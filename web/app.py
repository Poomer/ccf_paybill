from flask import Flask, request, redirect 
from flask.templating import render_template
import random
import pandas as pd 
#import openpyxl

app = Flask(__name__)

'''
@app.route("/")
def hello():
    return "Welcome to CCF 1976 Paybill System !"
'''

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route("/bill")
def calculate():
    num = random.randint(1,10) 
    return f"The lucky number is {num**2}"

@app.route("/ccf_bill")
def add_data():
    return render_template("add_bill.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        df = pd.read_excel(file)
        return df.to_html()

if __name__ == '__main__':
    app.run(debug=True)