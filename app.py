from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    year = db.Column(db.Integer)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author =db.Column(db.String(100))
    year = db.Column(db.Integer)


@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)


@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_book = Book(title=request.form['title'], author=request.form['author'], year=request.form['year'])
        db.session.add(new_book)
        db.session.commit()
        return redirect('/')
    return render_template('add_book.html')
    
    
@app.route('/edit_book/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = Book.query.get(book_id)
    
    if request.method == 'POST':
        # Update the book details based on the form data 
        book.title = request.form['title']
        book.author = request.form['author']
        book.year = int(request.form['year'])
        db.session.commit()
        return redirect('/')
    return render_template('edit_book.html', book=book)


@app.route('/delete/<int:id>')
def delete_book(id):
    book_to_delete = Book.query.get_or_404(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


