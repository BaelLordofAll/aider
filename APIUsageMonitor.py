from abacusai import ApiClient, UsageMonitor
from flask import Flask, render_template, request
import json

client = ApiClient(api_key='your_api_key')
app = Flask(__name__)

# Create a usage monitor project
usage_monitor = UsageMonitor(client, 'API Usage Monitor')

def load_api_limits():
    with open('api_limits.json', 'r') as file:
        return json.load(file)

@app.route('/')
def index():
    return render_template('api_usage.html')

@app.route('/check_usage')
def check_usage():
    limits = load_api_limits()
    usage = usage_monitor.check_usage(limits)
    return render_template('usage_report.html', usage=usage)

if __name__ == '__main__':
    app.run(debug=True)
