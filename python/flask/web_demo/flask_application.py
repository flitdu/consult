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


if __name__ == "__main__":
    app.run('0.0.0.0',port=8002)