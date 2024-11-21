# Full Stack = Front End (html,css,js) + Back End (js or java or python)

#Learning to use Flask
from dotenv import load_dotenv
load_dotenv()
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"