from flask import Flask, render_template, request
import config
import json
import MySQLdb

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/vid")
def vid():
    return render_template("vid.html")

@app.route('/card_search', methods=['POST', 'GET'])
def card_search():
    con = MySQLdb.connect(
        host=config.HOST,
        user=config.USER,
        password=config.PASSWORD,
        database=config.DATABASE
    )
    cur = con.cursor()

    cur.execute("SELECT details FROM cards")
    tuple = json.loads(cur.fetchall())
    cards = []
    images = []

    for card in tuple:
        cards.append(json.loads(card))
    for card in cards:
        images.append(card["images"]["small"])

    cur.close()
    con.close()
    return render_template("card_search.html", images = images)

@app.route("/card")
def card():
    return render_template("card.html", card=card)

@app.route("/card_listing")
def card_listing():
    return render_template("card_listing.html")