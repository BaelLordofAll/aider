from flask import Flask, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/ci_cd')
def ci_cd():
    try:
        # Run linting
        subprocess.run(["flake8", "."], check=True)
        
        # Run unit tests
        subprocess.run(["python", "-m", "unittest", "discover", "tests"], check=True)
        
        # Run integration tests
        subprocess.run(["python", "-m", "pytest", "tests/integration"], check=True)
        
        # If tests pass, proceed with deployment
        subprocess.run(["git", "pull"], check=True)
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
        
        # Deploy to staging
        subprocess.run(["flask", "deploy", "--env", "staging"], check=True)
        
        # If staging deployment is successful, deploy to production
        subprocess.run(["flask", "deploy", "--env", "production"], check=True)
        
        return jsonify({"status": "CI/CD pipeline completed successfully"})
    except subprocess.CalledProcessError as e:
        return jsonify({"status": "CI/CD pipeline failed", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
