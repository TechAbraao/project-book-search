from flask import Flask

def create_app():
    app = Flask(__name__)

    from src.app.resources.endpoints.home_route import home
    from src.app.resources.endpoints.new_book_route import new_book

    app.register_blueprint(home, url_prefix="/home")
    app.register_blueprint(new_book, url_prefix="/new-book")

    return app