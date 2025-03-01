from flask import Blueprint, render_template
from dotenv import load_dotenv
import os
from faker import Faker
from .utils.api_google_books import ApiGoogleBooks

load_dotenv()
API_KEY = os.getenv("API_KEY")
api_google_books = ApiGoogleBooks(API_KEY)

list_one = api_google_books.catchIdBook("Comédia")
list_two = api_google_books.catchIdBook("Drama")
list_three = api_google_books.catchIdBook("Romance")
list_four = api_google_books.catchIdBook("Suspense")
list_five = api_google_books.catchIdBook("Fantasia")
list_all = list_one + list_two + list_three + list_four + list_five

new_book = Blueprint('new_book', __name__)

@new_book.route("/")
def new_book_page():
    random = api_google_books.random_id(list_all)
    data = api_google_books.idForVolume(random)
    return render_template("pages/new_book/new_book.html", data=data)
