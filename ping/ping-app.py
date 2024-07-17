from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Get Pong service URL from environment variables
pong_service_url = os.getenv('PONG_SERVICE_URL', 'http://localhost:5001/pong')

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "Ping received"})

@app.route('/call-pong', methods=['GET'])
def call_pong():
    try:
        response = requests.get(pong_service_url)
        return jsonify({"message": "Ping called Pong", "pong_response": response.json()})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)