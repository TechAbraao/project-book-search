from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def root():
    return redirect(url_for('home'))

@app.route("/home")
def home():
    return render_template("pages/template/template.html", titulo="Book Search")

if __name__ == "__main__":
    app.run(debug=True)