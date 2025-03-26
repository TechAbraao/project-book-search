from src.app.utils import api_google_books
from flask import Blueprint, render_template


new_book = Blueprint('new_book', __name__)

@new_book.route("/<string:id>")
def new_book_page(id):
    data = api_google_books.idForVolume(id)
    return render_template("pages/new_book/new_book.html", data=data)
