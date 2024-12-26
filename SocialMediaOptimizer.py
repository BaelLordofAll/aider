from abacusai import ApiClient, SocialMediaOptimizer
from flask import Flask, render_template, request
import json

client = ApiClient(api_key='your_api_key')
app = Flask(__name__)

# Create a social media optimizer project
social_optimizer = SocialMediaOptimizer(client, 'Social Media Optimizer')

def load_platform_algorithms():
    with open('platform_algorithms.json', 'r') as file:
        return json.load(file)

@app.route('/')
def index():
    return render_template('social_media_optimization.html')

@app.route('/optimize_content', methods=['POST'])
def optimize_content():
    content = request.form['content']
    platform = request.form['platform']
    algorithms = load_platform_algorithms()
    
    optimized_content = social_optimizer.optimize_content(
        content=content,
        platform=platform,
        algorithms=algorithms
    )
    return render_template('optimized_content.html', optimized_content=optimized_content)

if __name__ == '__main__':
    app.run(debug=True)
