
import gym

env = gym.make('CartPole-v1')       # 实例化一个游戏环境，参数为游戏名称
state = env.reset()                 # 初始化环境，获得初始状态
while True:
    env.render()                    # 对当前帧进行渲染，绘图到屏幕
    action = model.predict(state)   # 假设我们有一个训练好的模型，能够通过当前状态预测出这时应该进行的动作
    next_state, reward, done, info = env.step(action)   # 让环境执行动作，获得执行完动作的下一个状态，动作的奖励，游戏是否已结束以及额外信息
    if done:                        # 如果游戏结束则退出循环
        break





if __name__ == '__main__':
    env = gym.make('CartPole-v1')       # 实例化一个游戏环境，参数为游戏名称
    model = QNetwork()
    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
    replay_buffer = deque(maxlen=10000) # 使用一个 deque 作为 Q Learning 的经验回放池
    epsilon = initial_epsilon
    for episode_id in range(num_episodes):
        state = env.reset()             # 初始化环境，获得初始状态
        epsilon = max(                  # 计算当前探索率
            initial_epsilon * (num_exploration_episodes - episode_id) / num_exploration_episodes,
            final_epsilon)
        for t in range(max_len_episode):
            env.render()                                # 对当前帧进行渲染，绘图到屏幕
            if random.random() < epsilon:               # epsilon-greedy 探索策略，以 epsilon 的概率选择随机动作
                action = env.action_space.sample()      # 选择随机动作（探索）
            else:
                action = model.predict(np.expand_dims(state, axis=0)).numpy()   # 选择模型计算出的 Q Value 最大的动作
                action = action[0]

            # 让环境执行动作，获得执行完动作的下一个状态，动作的奖励，游戏是否已结束以及额外信息
            next_state, reward, done, info = env.step(action)
            # 如果游戏Game Over，给予大的负奖励
            reward = -10. if done else reward
            # 将(state, action, reward, next_state)的四元组（外加 done 标签表示是否结束）放入经验回放池
            replay_buffer.append((state, action, reward, next_state, 1 if done else 0))
            # 更新当前 state
            state = next_state

            if done:                                    # 游戏结束则退出本轮循环，进行下一个 episode
                print("episode %4d, epsilon %.4f, score %4d" % (episode_id, epsilon, t))
                break

            if len(replay_buffer) >= batch_size:
                # 从经验回放池中随机取一个批次的四元组，并分别转换为 NumPy 数组
                batch_state, batch_action, batch_reward, batch_next_state, batch_done = \
                    map(np.array, zip(*random.sample(replay_buffer, batch_size)))

                q_value = model(batch_next_state)
                y = batch_reward + (gamma * tf.reduce_max(q_value, axis=1)) * (1 - batch_done)  # 计算 y 值
                with tf.GradientTape() as tape:
                    loss = tf.keras.losses.mean_squared_error(  # 最小化 y 和 Q-value 的距离
                        y_true=y,
                        y_pred=tf.reduce_sum(model(batch_state) * tf.one_hot(batch_action, depth=2), axis=1)
                    )
                grads = tape.gradient(loss, model.variables)
                optimizer.apply_gradients(grads_and_vars=zip(grads, model.variables))       # 计算梯度并更新参数