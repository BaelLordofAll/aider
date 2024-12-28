from flask import Flask, request, jsonify
from AutoAutomator import AutoAutomator

app = Flask(__name__)
auto_automator = AutoAutomator()

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    feedback = request.json.get('feedback')
    # Process feedback, perhaps store it or use it to improve the system
    auto_automator.learn_from_interactions(feedback)
    return jsonify({"status": "Feedback received and processed"})

if __name__ == '__main__':
    app.run(debug=True)
