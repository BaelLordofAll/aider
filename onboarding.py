from flask import Flask, render_template, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

@app.route('/')
def index():
    return render_template('onboarding.html')

@app.route('/start_onboarding', methods=['POST'])
def start_onboarding():
    user_data = request.json
    username = user_data.get('username')
    password = user_data.get('password')
    
    # Hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    # Here you would typically save this to a database
    # For simplicity, we'll just return the hashed password
    access_token = create_access_token(identity=username)
    
    # Start tutorial or guide user through initial setup
    return jsonify({"status": "Onboarding process started", "user_data": user_data, "token": access_token})

@app.route('/verify_user', methods=['POST'])
def verify_user():
    # Implement user verification logic here
    return jsonify({"status": "User verification completed"})

@app.route('/tutorial', methods=['GET'])
def tutorial():
    return render_template('tutorial.html')

if __name__ == '__main__':
    app.run(debug=True)
