from abacusai import ApiClient, TrendAnalyzer
from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime
import schedule
import time
from threading import Thread

client = ApiClient(api_key='your_api_key')
app = Flask(__name__)

# Create a trend analyzer project
trend_analyzer = TrendAnalyzer(client, 'Trend Analyzer')

def analyze_trends():
    # Implement logic to analyze trends from various sources
    trends = trend_analyzer.analyze_trends()
    with open('current_trends.json', 'w') as file:
        json.dump(trends, file)
    return trends

@app.route('/')
def index():
    return render_template('trend_analysis.html')

@app.route('/analyze_trends', methods=['POST'])
def analyze_trends_route():
    trends = analyze_trends()
    return jsonify({"status": "Trends analyzed.", "trends": trends})

@app.route('/schedule_trend_analysis', methods=['POST'])
def schedule_trend_analysis():
    interval = int(request.form['interval'])
    schedule.every(interval).minutes.do(analyze_trends)
    Thread(target=run_continuously).start()
    return jsonify({"status": f"Trend analysis scheduled every {interval} minutes."})

def run_continuously():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    app.run(debug=True)
