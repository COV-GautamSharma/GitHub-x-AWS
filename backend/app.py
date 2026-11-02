from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/api/hello")
def hello():
    return jsonify(message="Hello from the Python backend 🐍")