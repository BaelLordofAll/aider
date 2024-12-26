from abacusai import ApiClient, MemeGenerator
from flask import Flask, render_template, request

client = ApiClient(api_key='your_api_key')
app = Flask(__name__)

# Create a meme generator project
meme_generator = MemeGenerator(client, 'Meme Engine')

@app.route('/')
def index():
    return render_template('meme_creation.html')

@app.route('/create_meme', methods=['POST'])
def create_meme():
    template = request.form['template']
    text = request.form['text']
    
    meme = meme_generator.create_meme(
        template=template,
        text=text
    )
    return render_template('meme_preview.html', meme=meme)

if __name__ == '__main__':
    app.run(debug=True)
