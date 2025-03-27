from flask import Flask

def create_app():
    app = Flask(__name__)

    from src.app.resources.endpoints.Start import start
    from src.app.resources.endpoints.Home import home
    from src.app.resources.endpoints.NewBook import new_book

    app.register_blueprint(home)
    app.register_blueprint(new_book)
    app.register_blueprint(start)

    return app