from flask import Flask, request, jsonify
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route('/')
def index():
    return "Hey, welcome to the load balancer!"

@app.route('/balance_load', methods=['POST'])
def balance_load():
    # Logic to distribute load across servers
    return jsonify({"status": "Load balanced."})

if __name__ == '__main__':
    app.run(debug=True)
