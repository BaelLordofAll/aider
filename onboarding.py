from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('onboarding.html')

@app.route('/start_onboarding', methods=['POST'])
def start_onboarding():
    user_data = request.json
    # Here you would process user data, perhaps save it to a database or perform initial setup
    return jsonify({"status": "Onboarding process started", "user_data": user_data})

if __name__ == '__main__':
    app.run(debug=True)
