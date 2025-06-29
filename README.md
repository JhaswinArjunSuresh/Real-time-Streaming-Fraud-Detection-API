# ⚡ Real-time Streaming Fraud Detection

Consumes transaction data from Kafka, predicts fraud, and sends alerts to a FastAPI server.

## How it works
- `consumer.py` listens on Kafka topic `transactions`.
- Each message -> `predict_transaction` (RandomForest).
- If fraud, sends POST `/alert`.

## Usage
Run your Kafka broker first.  
Then start FastAPI:
```bash
uvicorn app.main:app --reload

