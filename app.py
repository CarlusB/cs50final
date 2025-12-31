import os
from flask import Flask, render_template, request
from pokemontcgsdk import Card # type: ignore
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

pokemontcg_io_api_key = os.environ.get("POKEMONTCG_IO_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/vid")
def vid():
    return render_template("vid.html")

@app.route('/card_search', methods=['POST', 'GET'])
def card_search():
    cards = None
    if request.method == 'POST':
        try:
            cards = Card.where(q='set.name:generations supertype:pokemon')
            return render_template("card_search.html", cards=cards)
        except KeyError:
            return render_template("error.html", 400)
    else:
        return render_template("card_search.html")

@app.route("/card")
def card():
    card = Card.find('xy1-1')
    return render_template("card.html", card=card)

@app.route("/card_listing")
def card_listing():
    return render_template("card_listing.html")