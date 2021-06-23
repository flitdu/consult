

import scipy.misc


img_array =scipy.misc.imread('my_own.png', flatten=True)
print(img_array)
img_data = 255 - img_array.reshape(784)  # 逆转黑白显示，mnist 中 0-->白
