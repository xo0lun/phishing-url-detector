"""
api.py

FastAPI application for phishing URL detection.
"""

from fastapi import FastAPI
from pydantic import BaseModel

from predict import predict_url


app = FastAPI(
    title="Phishing URL Detector",
    version="1.0.0",
)


class URLRequest(BaseModel):
    url: str


@app.get("/")
def home():
    return {
        "message": "Phishing URL Detector API"
    }


@app.post("/predict")
def predict(request: URLRequest):

    return predict_url(request.url)
