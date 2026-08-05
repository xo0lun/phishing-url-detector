# Phishing URL Detector

A machine learning project for detecting phishing URLs using feature engineering, supervised learning, and a REST API built with FastAPI.

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Latest-orange.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-API-success.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## Overview

Phishing attacks remain one of the most common cyber threats.

This project demonstrates how Machine Learning can be used to classify URLs as **legitimate** or **phishing** based on engineered features extracted from the URL itself.

The repository includes:

- Feature Engineering
- Model Training
- Model Evaluation
- REST API
- Unit Tests
- Reproducible Pipeline

---

## Features

- URL feature extraction
- Data preprocessing
- Random Forest classifier
- Model persistence using Joblib
- REST API with FastAPI
- Evaluation metrics
- Unit tests

---

## Project Structure

```text
phishing-url-detector/
│
├── data/
├── models/
├── notebooks/
├── src/
├── tests/
└── app.py
```

---

## Installation

```bash
git clone https://github.com/your-username/phishing-url-detector.git

cd phishing-url-detector

pip install -r requirements.txt
```

---

## Training

```bash
python src/train.py
```

---

## Running the API

```bash
uvicorn src.api:app --reload
```

---

## License

MIT License
