from flask import Flask
from services.fraud_service import load_transactions, detect_suspicious_devices

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "project": "Fraud Detection Graph System",
        "status": "running"
    }


@app.route("/load-data")
def load_data():
    return load_transactions()


@app.route("/suspicious-devices")
def suspicious_devices():
    return {
        "suspicious_devices": detect_suspicious_devices()
    }


if __name__ == "__main__":
    app.run(debug=True)