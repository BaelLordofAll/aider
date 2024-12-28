from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class APIResource(Resource):
    def get(self):
        return jsonify({
            "endpoints": [
                {
                    "path": "/monitor",
                    "method": "GET",
                    "description": "Monitor system performance metrics.",
                    "response": "JSON object with system metrics"
                },
                {
                    "path": "/learn",
                    "method": "POST",
                    "description": "Initiate learning process from user interactions.",
                    "response": "JSON object with status message"
                },
                # Add more endpoints here
            ]
        })

api.add_resource(APIResource, '/api-docs')

if __name__ == '__main__':
    app.run(debug=True)
