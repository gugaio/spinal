from flask import Flask, request, jsonify
from spinal import SpinalController
from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)  # Enable CORS for all routes and support credentials

controller = SpinalController()

@app.route('/ping', methods=['GET'])
def ping():
    response.headers.add('Access-Control-Allow-Origin', '*')
    return jsonify({'message': 'Pong!'}), 200

@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    if 'messages' in data:
        messages = data['messages']
        tools = data['tools'] if 'tools' in data else None
        responseMessage = controller.handle(messages, tools)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return jsonify({'message': responseMessage}), 200
    else:
        return jsonify({'error': 'No message attribute found'}), 400

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response
    
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
