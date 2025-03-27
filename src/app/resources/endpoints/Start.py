from flask import Blueprint, redirect, url_for

start = Blueprint('start', __name__, url_prefix='/')

@start.route("/", methods=["GET"])
def index():
    return redirect(url_for("home.index"))
