from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/health')
def health():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    
    if cpu_usage > 90 or memory_usage > 90 or disk_usage > 90:
        return jsonify({"status": "Warning", "details": {
            "cpu_usage": cpu_usage,
            "memory_usage": memory_usage,
            "disk_usage": disk_usage
        }}), 503
    else:
        return jsonify({"status": "Healthy", "details": {
            "cpu_usage": cpu_usage,
            "memory_usage": memory_usage,
            "disk_usage": disk_usage
        }})

if __name__ == '__main__':
    app.run(debug=True)
