from flask import Flask, render_template,request
import requests
import smtplib
import os


my_email = 'automobilemusic@gmail.com'


posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET','POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html", head_text = "Contact Me")
    
    elif request.method =='POST':
        with smtplib.SMTP("smtp.gmail.com") as connection:
            #security setup 
            connection.starttls()
            #login and send mail
            connection.login(user = my_email, password = os.environ.get('GMAIL_CODE'))
            connection.sendmail(
                    from_addr = request.form['email'],
                    to_addrs = my_email,
                    msg = f"{request.form['message']}\nname: {request.form['name']}\nemail: {request.form['email']}\nphone: {request.form['phone']}" )

        return render_template("contact.html", head_text = 'Succesfully Sent Message')


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
