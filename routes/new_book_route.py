from flask import Blueprint, abort, render_template
import requests
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = 'https://www.googleapis.com/books/v1/volumes?q={query}'
response = requests.get(URL + API_KEY)
res = response.json()

for items in res["items"]:
    volume_info = items["volumeInfo"]
    title = volume_info.get("title")
    description = volume_info.get("description")
    authors = volume_info.get("authors")
    categories = volume_info.get("categories")
    image = volume_info.get("imageLinks")
    data = {
        "title": title,
        "description": description,
        "authors": authors,
        "categories": categories,
        "image" : image['thumbnail'],
    }

new_book = Blueprint('new_book', __name__)

@new_book.route("/")
def new_book_page():
    return render_template("pages/new_book/new_book.html", data=data)
