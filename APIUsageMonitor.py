from abacusai import ApiClient, UsageMonitor
from flask import Flask, render_template, request

client = ApiClient(api_key='your_api_key')
app = Flask(__name__)

# Create a usage monitor project
usage_monitor = UsageMonitor(client, 'API Usage Monitor')

@app.route('/')
def index():
    return render_template('api_usage.html')

@app.route('/check_usage')
def check_usage():
    usage = usage_monitor.check_usage()
    return render_template('usage_report.html', usage=usage)

if __name__ == '__main__':
    app.run(debug=True)
