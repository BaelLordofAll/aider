from abacusai import ApiClient, AvatarCreator
from flask import Flask, render_template, request

client = ApiClient(api_key='your_api_key')
app = Flask(__name__)

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
    return render_template('avatar_preview.html', avatar=avatar)

@app.route('/integrate_social_media')
def integrate_social_media():
    avatar_project.integrate_with_social_media()
    return "Social media integration completed."

if __name__ == '__main__':
    app.run(debug=True)
