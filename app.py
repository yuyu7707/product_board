import random

from flask import Flask, render_template

app = Flask(__name__)

PRODUCTS = [
    {"name": "りんご（ふじ）", "price": 300, "producer_name": "高橋農園"},
    {"name": "八幡平マッシュルーム", "price": 450, "producer_name": "松尾きのこ園"},
    {"name": "ほうれん草", "price": 150, "producer_name": "西根ファーム"},
]


@app.route("/")
def index():
    return render_template("products/index.html", products=PRODUCTS)
