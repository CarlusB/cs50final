from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/vid")
def vid():
    return render_template("vid.html")

@app.route("/card_search")
def card_search():
    return render_template("card_search.html")

@app.route("/card")
def card():
    return render_template("card.html")

@app.route("/card_listing")
def card_listing():
    return render_template("card_listing.html")