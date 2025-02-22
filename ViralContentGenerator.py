from abacusai import ApiClient, ContentGenerator
from flask import Flask, render_template, request
import json

client = ApiClient(api_key='your_api_key')
app = Flask(__name__)

# Create a content generator project
content_generator = ContentGenerator(client, 'Viral Content Generator')

def load_trends():
    with open('current_trends.json', 'r') as file:
        return json.load(file)

@app.route('/')
def index():
    return render_template('viral_content.html')

@app.route('/generate_content', methods=['POST'])
def generate_content():
    topic = request.form['topic']
    format = request.form['format']
    target_audience = request.form['target_audience']
    trends = load_trends()
    
    content = content_generator.generate_content(
        topic=topic,
        format=format,
        target_audience=target_audience,
        trends=trends
    )
    return render_template('content_preview.html', content=content)

if __name__ == '__main__':
    app.run(debug=True)
