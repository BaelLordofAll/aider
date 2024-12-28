import logging
from flask import Flask, jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='system.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

@app.errorhandler(Exception)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # Log the error
    logging.error(f"An error occurred: {str(e)}", exc_info=True)
    # Return a JSON response with the error details
    return jsonify({
        'error': str(e),
        'message': 'An error occurred while processing your request.'
    }), 500

@app.errorhandler(404)
def not_found_error(error):
    logging.warning(f"404 Error: {error}")
    return jsonify({
        'error': 'Not found',
        'message': 'The requested resource could not be found.'
    }), 404

@app.errorhandler(400)
def bad_request_error(error):
    logging.warning(f"400 Error: {error}")
    return jsonify({
        'error': 'Bad Request',
        'message': 'The request was invalid or cannot be processed.'
    }), 400

@app.errorhandler(500)
def internal_server_error(error):
    logging.critical(f"500 Error: {error}")
    return jsonify({
        'error': 'Internal Server Error',
        'message': 'An unexpected condition was encountered.'
    }), 500

# Add more error handlers as needed
