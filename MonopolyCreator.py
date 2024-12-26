from abacusai import ApiClient, MonopolyCreator
from flask import Flask, render_template, request

client = ApiClient(api_key='your_api_key')
app = Flask(__name__)

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
    return "Rules defined."

@app.route('/create_game')
def create_game():
    monopoly_project.create_game()
    return "Game created."

@app.route('/integrate_real_estate')
def integrate_real_estate():
    monopoly_project.integrate_with_real_estate_market()
    return "Real estate integration completed."

if __name__ == '__main__':
    app.run(debug=True)
