from abacusai import ApiClient, ViralMarketingAI
from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime
import schedule
import time
from threading import Thread

client = ApiClient(api_key='your_api_key')
app = Flask(__name__)

# Create a viral marketing AI project
viral_marketing = ViralMarketingAI(client, 'Viral Marketing AI')

def load_trends():
    with open('current_trends.json', 'r') as file:
        return json.load(file)

def optimize_content(content, target_audience, trends):
    # Implement logic to optimize content based on trends and audience
    return viral_marketing.optimize_content(content, target_audience, trends)

@app.route('/')
def index():
    return render_template('viral_marketing.html')

@app.route('/suggest_strategy', methods=['POST'])
def suggest_strategy():
    content = request.form['content']
    target_audience = request.form['target_audience']
    trends = load_trends()
    
    strategy = viral_marketing.suggest_strategy(
        content=content,
        target_audience=target_audience,
        trends=trends
    )
    optimized_content = optimize_content(content, target_audience, trends)
    return render_template('strategy_preview.html', strategy=strategy, optimized_content=optimized_content)

@app.route('/update_trends', methods=['POST'])
def update_trends():
    # Logic to update trends from external sources or user input
    trends = load_trends()
    viral_marketing.update_trends(trends)
    return jsonify({"status": "Trends updated."})

if __name__ == '__main__':
    app.run(debug=True)
