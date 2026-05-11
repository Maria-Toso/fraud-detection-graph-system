from flask import Flask
from src.services.fraud_service import load_transactions

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


if __name__ == "__main__":
    app.run(debug=True)