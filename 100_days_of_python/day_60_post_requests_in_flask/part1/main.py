from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, request
import requests


app = Flask(__name__)




@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/login", methods=['GET','POST'])
def recieve_data():
    name = request.form['name']
    password = request.form['password']
    return f'<h1>{name},{password}'

     
if __name__ == '__main__':
    app.run(debug=True)
    