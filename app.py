from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin

@app.route('/')
def home():
    return "Flask backend for YouTube downloader"

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    url = data.get('url')
    print(f"Received URL: {url}")  # Debug line
    return jsonify({'message': f'Video URL received: {url}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)