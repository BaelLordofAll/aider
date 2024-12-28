from flask import Flask, request, jsonify
from werkzeug.contrib.fixers import ProxyFix
import random

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

class LoadBalancer:
    def __init__(self):
        self.servers = ['server1', 'server2', 'server3']
        self.weights = [1, 2, 1]  # Example weights for servers

    def balance_load(self, load):
        # Implement a weighted round-robin load balancing algorithm
        total_weight = sum(self.weights)
        r = random.uniform(0, total_weight)
        for i, server in enumerate(self.servers):
            r -= self.weights[i]
            if r <= 0:
                return server

load_balancer = LoadBalancer()

@app.route('/')
def index():
    return "What's up, welcome to the load balancer!"

@app.route('/balance_load', methods=['POST'])
def balance_load():
    load = request.json.get('load', 0)
    server = load_balancer.balance_load(load)
    return jsonify({"status": "Load balanced.", "server": server})

if __name__ == '__main__':
    app.run(debug=True)
