from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from dotenv import load_dotenv
import os
from .utils.api_google_books import ApiGoogleBooks

load_dotenv()
API_KEY = os.getenv("API_KEY")
api_google_books = ApiGoogleBooks(API_KEY)

home = Blueprint('home', __name__)

@home.route("/")
def home_page():
    try:
        list_one = api_google_books.catchIdBook("Fantasia")
        list_two = api_google_books.catchIdBook("Humor")
        list_all = list_one + list_two

        id1 = api_google_books.random_id(list_all)
        id2 = api_google_books.random_id(list_all)
        id3 = api_google_books.random_id(list_all)
        id4 = api_google_books.random_id(list_all)
        id5 = api_google_books.random_id(list_all)
        id6 = api_google_books.random_id(list_all)

        data1 = api_google_books.idForVolume(id1)
        data2 = api_google_books.idForVolume(id2)
        data3 = api_google_books.idForVolume(id3)
        data4 = api_google_books.idForVolume(id4)
        data5 = api_google_books.idForVolume(id5)
        data6 = api_google_books.idForVolume(id6)

        data = [data1, data2, data3, data4, data5, data6]

        return render_template("pages/template/template.html", titulo="Book Search", data = data)

    except TemplateNotFound:
        abort(404)
