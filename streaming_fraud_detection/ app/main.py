from fastapi import FastAPI, Request

app = FastAPI()

alerts = []

@app.post("/alert")
async def alert_endpoint(req: Request):
    payload = await req.json()
    alerts.append(payload)
    print(f"🚨 Alert stored: {payload}")
    return {"status": "alert received"}

@app.get("/alerts")
def get_alerts():
    return {"alerts": alerts}

@app.get("/health")
def health():
    return {"status": "ok"}

