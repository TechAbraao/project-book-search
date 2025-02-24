from flask import Flask
app = Flask(__name__)

from routes.routes import home

app.register_blueprint(home, url_prefix="/home")

if __name__ == "__main__":
    app.run(debug=True)