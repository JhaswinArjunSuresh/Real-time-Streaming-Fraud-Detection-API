import requests

def send_alert(transaction_data, probability):
    payload = {
        "transaction": transaction_data,
        "fraud_probability": probability
    }
    try:
        resp = requests.post("http://localhost:8000/alert", json=payload)
        print(f"Alert sent. Server response: {resp.text}")
    except Exception as e:
        print(f"Failed to send alert: {e}")

