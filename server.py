from flask import Flask, request, jsonify
from spinal import SpinalController
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

controller = SpinalController()

@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    if 'messages' in data:
        messages = data['messages']
        tools = data['tools'] if 'tools' in data else []
        responseMessage = controller.handle(messages, tools)
        return jsonify({'message': responseMessage}), 200
    else:
        return jsonify({'error': 'No message attribute found'}), 400

if __name__ == '__main__':
    app.run(debug=True)