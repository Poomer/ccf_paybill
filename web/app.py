from flask import Flask, request, redirect 
from flask.templating import render_template
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to CCF 1976 Paybill System !"

@app.route("/bill")
def calculate():
    num = random.randint(1,10) 
    return f"The lucky number is {num**2}"

@app.route("/ccf_bill")
def add_data():
    return render_template("add_bill.html")

if __name__ == '__main__':
    app.run()