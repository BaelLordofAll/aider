from abacusai import ApiClient, AvatarCreator
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import json
import os

client = ApiClient(api_key='your_api_key')
app = Flask(__name__)
socketio = SocketIO(app)

# Create an avatar project
avatar_project = AvatarCreator(client, 'Real-like Avatars')

@app.route('/')
def index():
    return render_template('avatar_customization.html')

@app.route('/create_avatar', methods=['POST'])
def create_avatar():
    name = request.form['name']
    age = int(request.form['age'])
    gender = request.form['gender']
    ethnicity = request.form['ethnicity']
    personality_traits = request.form.getlist('personality_traits')
    
    avatar_project.define_avatar(
        name=name,
        age=age,
        gender=gender,
        ethnicity=ethnicity,
        personality_traits=personality_traits
    )
    
    avatar = avatar_project.create_avatar()
    socketio.emit('avatar_created', {'message': 'Hey, your avatar is ready!'})
    return render_template('avatar_preview.html', avatar=avatar)

@app.route('/integrate_social_media')
def integrate_social_media():
    avatar_project.integrate_with_social_media()
    socketio.emit('social_media_integrated', {'message': 'Hey, your avatar is now social media savvy!'})
    return "Social media integration completed."

@app.route('/customize_avatar', methods=['POST'])
def customize_avatar():
    avatar_id = request.form['avatar_id']
    customization = request.form['customization']
    avatar_project.customize_avatar(avatar_id, customization)
    socketio.emit('avatar_customized', {'message': 'Hey, your avatar has been customized!'})
    return jsonify({"status": "Avatar customized."})

@app.route('/evolve_avatar', methods=['POST'])
def evolve_avatar():
    avatar_id = request.form['avatar_id']
    avatar_project.evolve_avatar(avatar_id)
    socketio.emit('avatar_evolved', {'message': 'Hey, your avatar just got a bit smarter!'})
    return jsonify({"status": "Avatar evolution initiated."})

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Hey, welcome aboard! You\'re now connected to the Avatar Creator.'})

if __name__ == '__main__':
    socketio.run(app, debug=True)
