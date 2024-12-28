from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/external_services')
def external_services():
    return jsonify({
        "services": [
            {
                "name": "Abacus.ai",
                "description": "Used for AI model training, deployment, and monitoring.",
                "api_key": "Required for authentication",
                "endpoints": [
                    {"path": "/train_model", "method": "POST", "description": "Train a new model"},
                    {"path": "/deploy_model", "method": "POST", "description": "Deploy a trained model"},
                    # Add more endpoints as needed
                ]
            },
            # Add more external services here
        ]
    })

if __name__ == '__main__':
    app.run(debug=True)
