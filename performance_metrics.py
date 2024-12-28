import psutil
import time
from flask import Flask, jsonify

app = Flask(__name__)

def get_system_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent
    network_io = psutil.net_io_counters()
    return {
        'cpu_usage': cpu_percent,
        'memory_usage': memory_percent,
        'disk_usage': disk_percent,
        'network_io': {
            'bytes_sent': network_io.bytes_sent,
            'bytes_recv': network_io.bytes_recv
        }
    }

@app.route('/metrics', methods=['GET'])
def metrics():
    return jsonify(get_system_metrics())

if __name__ == '__main__':
    app.run(debug=True)
