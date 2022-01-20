# -*- coding: utf-8 -*-
"""
==============================================================================
Time : 2022/1/17 10:17 下午
Author : Dufy
Email : 813540660@qq.com
File : flask_application.py


==============================================================================
"""

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route("/")
def index():
    name = request.args.get("name", "world")  # 默认值 world
    return render_template("index.html", PARA=name)
    # return "hello, world"


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")  # form 对应 post; args对应 get
    dorm = request.form.get("dorm")
    if not name or not dorm:
        # return "failure"
        return render_template("failure.html")
    else:
        return render_template("success.html")


if __name__ == "__main__":
    app.run('0.0.0.0',port=8001)