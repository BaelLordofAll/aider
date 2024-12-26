from abacusai import ApiClient
from flask import Flask, render_template, request, jsonify
from AutoAutomator import AutoAutomator
from SystemIntegration import SystemIntegration
from flask_socketio import SocketIO, emit
import json
from datetime import datetime
import schedule
import time
from threading import Thread

client = ApiClient(api_key='your_api_key')
app = Flask(__name__)
socketio = SocketIO(app)

class BaEl:
    def __init__(self):
        self.auto_automator = AutoAutomator()
        self.system_integration = SystemIntegration()
        self.scheduler = schedule.Scheduler()
        self.socketio = socketio
        self.is_running = False

    def evolve_system(self):
        if not self.is_running:
            self.is_running = True
            self.auto_automator.monitor_system()
            self.auto_automator.learn_from_interactions()
            self.auto_automator.evolve_system()
            self.system_integration.integrate_all()
            self.socketio.emit('system_evolved', {'message': 'System has evolved by Ba\'el'})
            self.is_running = False

    def schedule_evolution(self):
        self.scheduler.every().day.at("00:00").do(self.evolve_system)

    def run_scheduler(self):
        def run_continuously():
            while True:
                self.scheduler.run_pending()
                time.sleep(1)
        Thread(target=run_continuously).start()

    def auto_run_evolution(self):
        if not self.is_running:
            self.evolve_system()
            return "System evolution automatically initiated by Ba'el."
        return "System is currently evolving."

    def update_ui(self):
        # Logic to update UI with new system capabilities or changes
        pass

ba_el = BaEl()

@app.route('/')
def index():
    return render_template('ba_el.html')

@app.route('/evolve', methods=['POST'])
def evolve():
    ba_el.evolve_system()
    return jsonify({"status": "System evolution initiated by Ba'el."})

@app.route('/start_scheduler', methods=['POST'])
def start_scheduler():
    ba_el.schedule_evolution()
    ba_el.run_scheduler()
    return jsonify({"status": "Ba'el's scheduler started."})

@app.route('/auto_run_evolution', methods=['GET'])
def auto_run_evolution():
    return jsonify({"status": ba_el.auto_run_evolution()})

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected to Ba\'el'})

if __name__ == '__main__':
    socketio.run(app, debug=True)
