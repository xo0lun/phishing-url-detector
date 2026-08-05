"""
train.py

Train a phishing URL classifier.
"""

from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from features import extract_features


DATASET = Path("data/raw/urls.csv")
MODEL_PATH = Path("models/phishing_model.joblib")


def main():
    df = pd.read_csv(DATASET)

    X = pd.DataFrame(
        [extract_features(url) for url in df["url"]]
    )

    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print(classification_report(y_test, predictions))

    MODEL_PATH.parent.mkdir(exist_ok=True)

    joblib.dump(model, MODEL_PATH)

    print(f"Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    main()
