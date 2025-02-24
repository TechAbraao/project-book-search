from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

home = Blueprint('home', __name__)

@home.route("/")
def home_page():
    try:
        return render_template("pages/template/template.html", titulo="Book Search")
    except TemplateNotFound:
        abort(404)
