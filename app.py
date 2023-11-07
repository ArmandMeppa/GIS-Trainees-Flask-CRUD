from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app.debug = True
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    year = db.Column(db.Integer)


@app.before_request
def import_data_func():
    db.create_all()
    if Book.query.first() is None:  # Only import if table is empty
        data = pd.read_csv('data.csv')
        for row in data.itertuples():
            db.session.add(Book(title=row.title, author=row.author, year=row.year))
        db.session.commit()

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)