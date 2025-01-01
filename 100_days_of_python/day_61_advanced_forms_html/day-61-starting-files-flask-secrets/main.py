from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, ValidationError
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5





app = Flask(__name__)
app.config['SECRET_KEY'] = 'monkey'
bootstrap = Bootstrap5(app)

class LoginForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(),
        Length(min=2, max=50)
    ])
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(min=8)])
    
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8)
    ])
    submit = SubmitField('Log In')
      

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():  # This checks if it's a valid POST submission
        # Handle the login submission
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
                    return render_template("success.html")
        else:
            return render_template("denied.html")
        
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
