from verkefni_2 import app
from verkefni_2 import models as model
from flask import render_template


@app.route('/')
def index():
    booklist = model.booklist
    return render_template('index.html', booklist=booklist)



@app.route("/book/<isbn>")
def book(isbn=None):

    matched = isbn
    return render_template('book.html', matched=matched)