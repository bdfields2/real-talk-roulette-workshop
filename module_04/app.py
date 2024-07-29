from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

deck = []
players = []
scores = {}
MAX_SCORE = 3

def load_deck():
    global deck
    with open("questions.txt", "r") as questions:
        cards = questions.read().split("\n")
    random.shuffle(cards)
    deck = cards

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    global players, scores
    players = request.json.get('players')
    scores = {player: 0 for player in players}
    load_deck()
    return jsonify({'message': 'Game started', 'players': players})

@app.route('/draw_card', methods=['POST'])
def draw_card():
    if not deck:
        return jsonify({'message': 'No more cards in the deck.'})
    card = deck.pop(0)
    return jsonify({'card': card, 'remaining': len(deck)})

@app.route('/submit_winner', methods=['POST'])
def submit_winner():
    global scores
    winner = request.json.get('winner')
    if winner in scores:
        scores[winner] += 1
        if scores[winner] >= MAX_SCORE:
            return jsonify({'winner': winner, 'game_over': True})
    return jsonify({'scores': scores, 'game_over': False})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
