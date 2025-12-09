from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return Flask.render_template("index.html")

@app.route("/vid")
def vid():
    return Flask.render_template("vid.html")
