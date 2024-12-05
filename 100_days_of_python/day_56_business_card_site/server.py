from flask import Flask, render_template
import dotenv

dotenv.load_dotenv()

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    


