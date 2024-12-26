from abacusai import ApiClient
from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime
import schedule
import time
from threading import Thread

client = ApiClient(api_key='your_api_key')
app = Flask(__name__)

class LLMManager:
    def __init__(self):
        self.llms = {
            'gpt2': {'api_key': 'your_api_key', 'model': 'gpt2'},
            'huggingface': {'api_key': 'your_api_key', 'model': 'distilgpt2'},
            'free_llm': {'api_key': 'your_api_key', 'model': 'free_llm_model'}
        }
        self.current_llm = 'gpt2'
        self.scheduler = schedule.Scheduler()

    def switch_llm(self, llm_name):
        if llm_name in self.llms:
            self.current_llm = llm_name
            return f"Switched to {llm_name}"
        return "LLM not found"

    def get_llm(self):
        return self.llms[self.current_llm]

    def schedule_llm_switch(self, interval):
        self.scheduler.every(interval).minutes.do(self._switch_llm)

    def _switch_llm(self):
        llms = list(self.llms.keys())
        current_index = llms.index(self.current_llm)
        next_index = (current_index + 1) % len(llms)
        self.switch_llm(llms[next_index])

    def run_scheduler(self):
        while True:
            self.scheduler.run_pending()
            time.sleep(1)

llm_manager = LLMManager()

@app.route('/')
def index():
    return render_template('llm_manager.html')

@app.route('/switch_llm', methods=['POST'])
def switch_llm():
    llm_name = request.form['llm_name']
    return jsonify({"status": llm_manager.switch_llm(llm_name)})

@app.route('/schedule_llm_switch', methods=['POST'])
def schedule_llm_switch():
    interval = int(request.form['interval'])
    llm_manager.schedule_llm_switch(interval)
    llm_manager.run_scheduler()
    return jsonify({"status": f"LLM switch scheduled every {interval} minutes."})

if __name__ == '__main__':
    app.run(debug=True)
