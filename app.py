import random

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>八幡平 産直掲示板</h1><h2>今週の目玉！</h2><p>こんにちは、Falsk!</p>"


#@app.route("/hello/<name>")
#def hello(name):
    return f"<p>こんにちは{name}</p>"


@app.route("/omikuji")
def omikuji():
    # results = ["大吉", "中吉", "小吉", "吉", "凶"]

    # kekka = results[random.randint(0, 4)]  # 1〜4 のどれか

    # return f"<h3>あなたの運勢は{kekka}です！</h3>"

    omikujis = ["大吉", "中吉", "小吉", "吉", "凶"]
    unnsei = random.choice(omikujis)
    return f"<p>あなたの運勢は{unnsei}</p>"
