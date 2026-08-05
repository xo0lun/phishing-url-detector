"""
features.py

Feature extraction for phishing URL detection.
"""

from __future__ import annotations

import ipaddress
import re
from urllib.parse import urlparse

import pandas as pd


SUSPICIOUS_KEYWORDS = [
    "login",
    "verify",
    "secure",
    "update",
    "account",
    "bank",
    "paypal",
    "confirm",
    "signin",
]


def has_ip_address(url: str) -> int:
    """Return 1 if the hostname is an IP address."""

    try:
        host = urlparse(url).hostname

        if host is None:
            return 0

        ipaddress.ip_address(host)

        return 1

    except ValueError:
        return 0


def extract_features(url: str) -> dict:
    """
    Extract numerical features from a URL.
    """

    parsed = urlparse(url)

    hostname = parsed.netloc

    return {
        "url_length": len(url),
        "hostname_length": len(hostname),
        "path_length": len(parsed.path),
        "count_digits": sum(c.isdigit() for c in url),
        "count_dots": url.count("."),
        "count_hyphens": url.count("-"),
        "count_slashes": url.count("/"),
        "count_question_marks": url.count("?"),
        "count_equals": url.count("="),
        "count_at": url.count("@"),
        "count_percent": url.count("%"),
        "count_ampersand": url.count("&"),
        "https": int(parsed.scheme == "https"),
        "has_ip": has_ip_address(url),
        "suspicious_keywords": sum(
            keyword in url.lower()
            for keyword in SUSPICIOUS_KEYWORDS
        ),
    }

def features_to_dataframe(url: str) -> pd.DataFrame:
    """
    Convert extracted features into a DataFrame.
    """

    return pd.DataFrame([extract_features(url)])
