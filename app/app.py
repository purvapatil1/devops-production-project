import os
from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "development")
APP_NAME = os.getenv("APP_NAME", "DevOps Production Project")

@app.route("/")
def home():
    return jsonify({
        "message": APP_NAME,
        "environment": APP_ENV,
        "status": "Running",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
