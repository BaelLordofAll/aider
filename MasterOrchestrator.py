from abacusai import ApiClient
from flask import Flask, render_template, request, jsonify
from AutoAutomator import AutoAutomator
from SystemIntegration import SystemIntegration
from flask_socketio import SocketIO, emit
import json
from datetime import datetime
import schedule
import time

client = ApiClient(api_key='your_api_key')
app = Flask(__name__)
socketio = SocketIO(app)

class MasterOrchestrator:
    def __init__(self):
        self.auto_automator = AutoAutomator()
        self.system_integration = SystemIntegration()
        self.scheduler = schedule.Scheduler()
        self.socketio = socketio

    def orchestrate_system(self):
        self.auto_automator.monitor_system()
        self.auto_automator.learn_from_interactions()
        self.auto_automator.evolve_system()
        self.system_integration.integrate_all()
        self.socketio.emit('system_orchestrated', {'message': 'System has been orchestrated'})

    def schedule_orchestration(self):
        self.scheduler.every().day.at("00:00").do(self.orchestrate_system)

    def run_scheduler(self):
        while True:
            self.scheduler.run_pending()
            time.sleep(1)

    def auto_run_orchestration(self):
        self.orchestrate_system()
        return "System orchestration automatically initiated."

master_orchestrator = MasterOrchestrator()

@app.route('/')
def index():
    return render_template('master_orchestrator.html')

@app.route('/orchestrate', methods=['POST'])
def orchestrate():
    master_orchestrator.orchestrate_system()
    return jsonify({"status": "System orchestration initiated."})

@app.route('/start_orchestrator', methods=['POST'])
def start_orchestrator():
    master_orchestrator.schedule_orchestration()
    master_orchestrator.run_scheduler()
    return jsonify({"status": "Orchestrator started."})

@app.route('/auto_run_orchestration', methods=['GET'])
def auto_run_orchestration():
    return jsonify({"status": master_orchestrator.auto_run_orchestration()})

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})

if __name__ == '__main__':
    socketio.run(app, debug=True)
