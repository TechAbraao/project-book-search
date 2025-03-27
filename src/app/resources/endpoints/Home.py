from src.app.utils import api_google_books
from src.app.controllers.search_book_controller import FindingBook
from src.app.utils.GoogleBooksAPI import get_books_by_genre
from flask import Blueprint, render_template, abort, request, redirect, url_for
from jinja2 import TemplateNotFound

home = Blueprint('home', __name__, url_prefix="/home")

@home.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        try:
            data = get_books_by_genre(api_google_books, genre="Humor", num_books=6)
            return render_template("pages/template/template.html", titulo="Book Search", data = data)

        except TemplateNotFound:
            abort(404)
    if request.method == "POST":
        book_name = request.get_json()
        findBook = FindingBook(book_name)
        # idFindBook = findBook.get("id")
        # print(idFindBook)
        # print(type(idFindBook))
        # return redirect(url_for("new_book.index", id=idFindBook))
        return render_template("pages/new_book/new_book.html", data=findBook)