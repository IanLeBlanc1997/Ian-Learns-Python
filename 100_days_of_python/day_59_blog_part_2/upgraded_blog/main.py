from flask import Flask, render_template
import dotenv
import requests
from datetime import datetime


date = datetime.now().date()
response = requests.get('https://api.npoint.io/72a43712dd27f704a9ea')
data = response.json()

dotenv.load_dotenv()

app = Flask(__name__)

@app.route("/") 
def homepage():
    return render_template('index.html', data=data, date=date)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:value>")
def post(value):
    for post in data:
        if post['id'] == value:
            selected_post = post
            break
    return render_template("post.html",post=selected_post)


if __name__ == '__main__':
    app.run(debug=True)