from flask import Flask
app = Flask(__name__)
from routes.home_route import home
from routes.new_book_route import new_book

app.register_blueprint(home, url_prefix="/home")
app.register_blueprint(new_book, url_prefix="/new-book")

if __name__ == "__main__":
    app.run(debug=True)