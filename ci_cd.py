from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/ci_cd')
def ci_cd():
    try:
        # Run tests
        subprocess.run(["python", "-m", "unittest", "discover", "tests"], check=True)
        # If tests pass, proceed with deployment
        subprocess.run(["git", "pull"], check=True)
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
        subprocess.run(["flask", "deploy"], check=True)
        return jsonify({"status": "CI/CD pipeline completed successfully"})
    except subprocess.CalledProcessError as e:
        return jsonify({"status": "CI/CD pipeline failed", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
