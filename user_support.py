from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/submit_ticket', methods=['POST'])
def submit_ticket():
    ticket_data = request.json
    # Here you would process the ticket, perhaps send an email or store it in a ticketing system
    return jsonify({"status": "Support ticket submitted", "ticket_id": "TICKET-12345"})

if __name__ == '__main__':
    app.run(debug=True)
