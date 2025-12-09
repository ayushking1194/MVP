from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

from src.config_loader import load_config
from src.metrics import update_mock_metrics

app = FastAPI(title="Infra Capacity API")

CONFIG = load_config()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    update_mock_metrics()
    return PlainTextResponse(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )

@app.get("/config")
def get_config():
    return CONFIG

@app.post("/config/reload")
def reload_config():
    global CONFIG
    CONFIG = load_config()
    return {"status": "reloaded", "config": CONFIG}