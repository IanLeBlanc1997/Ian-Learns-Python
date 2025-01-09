from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_migrate import Migrate


class Base(DeclarativeBase):
    pass

                            #initializing the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book-ratings.db'
db=SQLAlchemy(model_class=Base)
db.init_app(app)

            #class for the table in the database                    
class BookRatings(db.Model):
    __tablename__ = 'Book Ratings'
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    title: Mapped[str] = mapped_column(String(250),unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable= False, unique=True)
    rating: Mapped[float] = mapped_column(Float, nullable = False, unique=False)

                    #run once to create table

# with app.app_context():
#     db.create_all()
with app.app_context():
    db.drop_all()
    db.create_all()

######################## HOME #############
@app.route('/')
def home():
                    #### read from the sql database
    with app.app_context():
        result = db.session.execute(db.select(BookRatings).order_by(BookRatings.id))
        ### This scalars().all() function turns the database query into an iterable (a list of dictionaries in this case)
        all_books = result.scalars().all()
    return render_template('index.html', all_books=all_books)

################# ADD ################
@app.route("/add", methods = ['GET','POST'])
def add():
    if request.method == 'POST':
        with app.app_context():
                                            #automatically makes a new id as new books are added
            new_book = BookRatings(title= request.form['name'] , author= request.form['author'], rating = request.form['rating'])
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


            ############## EDIT ###########
@app.route("/edit/<int:book_id>", methods = ['GET','POST'])
def edit(book_id):
    with app.app_context():
     entry = db.session.execute(db.select(BookRatings).where(BookRatings.id == book_id)).scalar()
    if request.method == 'POST':
        with app.app_context():
            book_to_update = db.session.execute(db.select(BookRatings).where(BookRatings.id == book_id)).scalar()
            book_to_update.rating = request.form['new_rating']
            db.session.commit() 
        return redirect(url_for('home'))
    return render_template('edit.html', entry=entry)
############## DELETE ################
@app.route("/delete/<int:book_id>", methods = ['GET','POST'])
def delete(book_id):
    with app.app_context():       
        book_to_delete=db.session.execute(db.select(BookRatings).where(BookRatings.id == book_id)).scalar() 
        db.session.delete(book_to_delete)           
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

