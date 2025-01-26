from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "SpeakX Flask API (HTTPS Secured!)."
@app.route('/status')
def status():
    return jsonify({
        "status": "API is up and Running."
    })
@app.route('/pic')
def show_pic():
    return send_from_directory('images', 'img.png')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
