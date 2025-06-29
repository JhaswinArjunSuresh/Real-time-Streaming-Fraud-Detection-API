from kafka import KafkaConsumer
import json
from .model import predict_transaction
from .alert_api import send_alert

def start_consumer():
    consumer = KafkaConsumer(
        'transactions',
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    print("🚀 Listening to Kafka topic 'transactions'...")
    for message in consumer:
        data = message.value
        print(f"Received: {data}")

        features = data["features"]  # Example: list of input features
        prediction, prob = predict_transaction(features)

        if prediction == 1:
            print(f"⚠️ Fraud detected with probability {prob}")
            send_alert(data, prob)

