from flask import Blueprint, render_template
from dotenv import load_dotenv
import os
from .utils.api_google_books import ApiGoogleBooks

load_dotenv()
API_KEY = os.getenv("API_KEY")

api_google_books = ApiGoogleBooks(API_KEY)

new_book = Blueprint('new_book', __name__)

@new_book.route("/<string:id>")
def new_book_page(id):
    data = api_google_books.idForVolume(id)
    return render_template("pages/new_book/new_book.html", data=data)
