from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    maps_link = StringField('Google Maps Link', validators=[DataRequired(), URL()])
    open_time = StringField("open Time", validators=[DataRequired()])
    close_time=StringField('close time', validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Goodness",None,choices=['☕️','☕️☕️','☕️☕️☕️','☕️☕️☕️☕️','☕️☕️☕️☕️☕️'])
    wifi_rating =SelectField("Wifi Goodness",None,choices=['☕️','☕️☕️','☕️☕️☕️','☕️☕️☕️☕️','☕️☕️☕️☕️☕️'])
    power_rating = SelectField("Power Goodness",None,choices=['☕️','☕️☕️','☕️☕️☕️','☕️☕️☕️☕️','☕️☕️☕️☕️☕️'])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods= ['GET','POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
      with open('/Users/ianleblanc/Desktop/Repositories/Ian-Learns-Python/100_days_of_python/day_62_coffee_site/day-62-starting-files-coffee-and-wifi/cafe-data.csv', newline='', encoding='utf-8',mode='a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([form.cafe.data,form.maps_link.data,form.open_time.data,form.close_time.data,form.coffee_rating.data,form.wifi_rating.data,form.power_rating.data])
 
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('/Users/ianleblanc/Desktop/Repositories/Ian-Learns-Python/100_days_of_python/day_62_coffee_site/day-62-starting-files-coffee-and-wifi/cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
