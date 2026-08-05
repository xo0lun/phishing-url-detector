"""
predict.py

Prediction utilities for the phishing URL detector.
"""

from pathlib import Path

import joblib

from features import extract_features


MODEL_PATH = Path("models/phishing_model.joblib")


class URLPredictor:
    """
    Load a trained model and predict whether a URL is phishing.
    """

    def __init__(self):
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                "Model not found. Run train.py first."
            )

        self.model = joblib.load(MODEL_PATH)

    def predict(self, url: str) -> dict:

        features = extract_features(url)

        prediction = self.model.predict([list(features.values())])[0]

        probability = self.model.predict_proba(
            [list(features.values())]
        )[0]

        confidence = float(max(probability))

        return {
            "url": url,
            "prediction": (
                "phishing"
                if prediction == 1
                else "legitimate"
            ),
            "confidence": round(confidence, 4),
        }


def predict_url(url: str):

    predictor = URLPredictor()

    return predictor.predict(url)
