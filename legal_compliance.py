from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/legal')
def legal():
    return jsonify({
        "gdpr": "We comply with GDPR regulations for data protection.",
        "ccpa": "We adhere to the California Consumer Privacy Act.",
        "data_protection": "All user data is encrypted and stored securely.",
        "terms_of_service": "Link to terms of service",
        "privacy_policy": "Link to privacy policy"
    })

if __name__ == '__main__':
    app.run(debug=True)
