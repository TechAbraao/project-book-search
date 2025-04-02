from src.app.utils import api_google_books
from flask import Blueprint, render_template


new_book = Blueprint('new_book', __name__, url_prefix="/new-book")

@new_book.route("/<string:id>", methods=["GET"])
def index(id):
    data = api_google_books.idForVolume(id)
    return render_template("layouts/new_book.html", data=data)
