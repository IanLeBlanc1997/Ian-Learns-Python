from flask import Flask, render_template, redirect, url_for, request, abort
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired
import requests

TMDB_token = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhOGU1MTkwZDk1ZWU5MWYzZTMwYTZmOTMyMTZlNzVhZSIsIm5iZiI6MTczNjU1ODk3NC42ODQsInN1YiI6IjY3ODFjOTdlYmQ3OTNjMDM1NDRlNTMwOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.oeSqROOD7_sK34FQAKZ2nA0c1atK5jvNvIujgThzrNg'
TMDB_key = 'a8e5190d95ee91f3e30a6f93216e75ae'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)



class Base(DeclarativeBase):
    pass

                            #initializing the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-10-movies.db'
db=SQLAlchemy(model_class=Base)
db.init_app(app)
migrate = Migrate(app,db)

            #class for the table in the database                    
class Movie(db.Model):
    __tablename__ = 'Top_10_Movies'
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    title: Mapped[str] = mapped_column(String(250),unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable= False)
    description: Mapped[str]= mapped_column(String(250))
    rating: Mapped[float] = mapped_column(Float, nullable =True)
    ranking: Mapped[int]=mapped_column(Integer, nullable =True)
    review: Mapped[str]=mapped_column(String, nullable =True)
    img_url: Mapped[str]=mapped_column(String)

                    #run once to create table

# with app.app_context():
#     db.create_all()

## REFRESH

# with app.app_context():
#     db.drop_all()
#     db.create_all()



class EditForm(FlaskForm):
    movie_rating = FloatField('Edit Movie Rating')
    movie_review = StringField("Edit Movie Review")
    submit = SubmitField("Submit")

class AddForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Submit')

############# HOME ###############

@app.route("/")
def home():
    with app.app_context():
        result = db.session.execute(db.select(Movie).order_by(Movie.rating.desc()))
        ### This scalars().all() function turns the database query into an iterable (a list of dictionaries in this case)
        all_movies = result.scalars().all()
        for movie in all_movies:
            print(f"Movie ID: {movie.id}, Rating: {movie.rating}")  # Debug print
    
    return render_template("index.html", all_movies = all_movies)

################# EDIT #############

@app.route('/edit/<movie_title>', methods= ['GET', 'POST'])
def edit(movie_title):
    form = EditForm()
    movie_to_update = db.session.execute(db.select(Movie).where(Movie.title==movie_title)).scalar()
    if not movie_to_update:
    # Handle case where movie doesn't exist
        return abort(404)
    
    if form.validate_on_submit():
        if form.movie_rating.data:
            movie_to_update.rating = form.movie_rating.data
            #Ranking system
            all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars().all()
            for n,movie in enumerate(all_movies,start=1):
                movie.ranking = n
                db.session.commit()
            # db.session.execute(db.select(Movie).order_by(Movie.rating))
            # db.session.commit()
        if form.movie_review.data:
            movie_to_update.review = form.movie_review.data
            db.session.commit()
        return redirect(url_for('home'))
        
    form.movie_rating.data = movie_to_update.rating
    return render_template('edit.html', form=form)

############### ADD ############

@app.route('/add', methods = ['GET','POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        return redirect(url_for('select', movie_title = form.title.data))

    return render_template("add.html", form=form)

####### SELECT #############

@app.route('/select/<movie_title>', methods = ['GET','POST'])
def select(movie_title):
    headers = {'accept':'application/json','Authorization': TMDB_token}
    parameters = {'query':movie_title}
    response = requests.get('https://api.themoviedb.org/3/search/movie', headers=headers, params=parameters)
    data = response.json()
    movies = data['results']


    return render_template('select.html', movies=movies, movie_title = movie_title)


################### POPULATE ##############

@app.route('/populate/<movie_title>/<int:movie_index>')
def populate(movie_title,movie_index):
    ############# API CALL ############
    headers = {'accept':'application/json','Authorization': TMDB_token}
    parameters = {'query':movie_title}
    response = requests.get('https://api.themoviedb.org/3/search/movie', headers=headers, params=parameters)
    data = response.json()
    ######### PARSING DATA INTO MOVIE OBJECT ###########
    new_movie = Movie(
    title= data['results'][movie_index]['original_title'],
    year=data['results'][movie_index]['release_date'].split('-')[0],
    description = data['results'][movie_index]['overview'],
    img_url= 'https://image.tmdb.org/t/p/original'+ str(data['results'][movie_index]['poster_path']))   
    db.session.add(new_movie)                   
    db.session.commit()
    return redirect(url_for('edit', movie_title=new_movie.title))

############# DELETE ############

@app.route('/delete/<int:movie_id>', methods = ['GET','POST'])
def delete(movie_id):
    movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id==movie_id)).scalar()
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(debug=True)
