from abacusai import ApiClient, MonopolyCreator
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import json

client = ApiClient(api_key='your_api_key')
app = Flask(__name__)
socketio = SocketIO(app)

# Create a monopoly project
monopoly_project = MonopolyCreator(client, 'Monopoly Creation')

@app.route('/')
def index():
    return render_template('monopoly_setup.html')

@app.route('/define_rules', methods=['POST'])
def define_rules():
    properties = request.form.getlist('properties')
    utilities = request.form.getlist('utilities')
    chance_cards = request.form.getlist('chance_cards')
    community_chest_cards = request.form.getlist('community_chest_cards')
    
    monopoly_project.define_rules(
        properties=properties,
        utilities=utilities,
        chance_cards=chance_cards,
        community_chest_cards=community_chest_cards
    )
    socketio.emit('rules_defined', {'message': 'Hey, the rules are set!'})
    return "Hey, rules defined."

@app.route('/create_game')
def create_game():
    monopoly_project.create_game()
    socketio.emit('game_created', {'message': 'Hey, the game is ready to play!'})
    return "Hey, game created."

@app.route('/integrate_real_estate')
def integrate_real_estate():
    monopoly_project.integrate_with_real_estate_market()
    socketio.emit('real_estate_integrated', {'message': 'Hey, real estate integration completed!'})
    return "Hey, real estate integration completed."

@app.route('/evolve_game', methods=['POST'])
def evolve_game():
    monopoly_project.evolve_game()
    socketio.emit('game_evolved', {'message': 'Hey, the game just got more interesting!'})
    return jsonify({"status": "Game evolution initiated."})

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Hey, welcome aboard! You\'re now connected to the Monopoly Creator.'})

if __name__ == '__main__':
    socketio.run(app, debug=True)
