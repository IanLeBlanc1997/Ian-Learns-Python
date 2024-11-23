from dotenv import load_dotenv
load_dotenv()
from flask import Flask
import random 
random_number=random.randint(1,9)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Guess a number between 0 and 9!</h1>\
            <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route('/<int:number>')
def compare(number):
    if number > random_number:
        return "<h1 style='text-align: center'>Too High!</h1>"
    if number < random_number:
        return "<h1 style='text-align: center'>Too Low!</h1>"
    if number == random_number:
        return "<h1 style='text-align: center'>You Got It!</h1>"

     
if __name__ == '__main__':
    app.run(debug=True)
    