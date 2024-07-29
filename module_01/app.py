from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

deck = []

def load_deck():
    global deck
    with open("questions.txt", "r") as questions:
        cards = questions.read().split("\n")
    random.shuffle(cards)
    deck = cards

@app.route('/')
def index():
    load_deck()
    return render_template('index.html')

@app.route('/draw_card', methods=['POST'])
def draw_card():
    if not deck:
        return jsonify({'message': 'No more cards in the deck.'})
    card = deck.pop(0)
    return jsonify({'card': card, 'remaining': len(deck)})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
