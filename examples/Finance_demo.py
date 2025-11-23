# pip install tqnn-client
"""
Finance demo for the TQNN AnyEngine API.

This example shows how to send a small window of derived financial
features into the API. In practice, you would build these features
from real OHLCV data (prices, volume, indicators, etc.).
"""

import os
from tqnn_client import TQNNClient


# Recommended: configure via environment variables
BASE_URL = os.getenv("TQNN_API_URL", "https://YOUR-TQNN-ENDPOINT")
API_KEY  = os.getenv("TQNN_API_KEY", "YOUR_TQNN_API_KEY")


def main():
    client = TQNNClient(api_key=API_KEY, base_url=BASE_URL)

    # ------------------------------------------------------------------
    # Example synthetic finance features.
    # Each row could represent:
    #   [normalized_close, rsi_14, macd, volatility]
    # Replace with real, precomputed features from your own pipeline.
    # ------------------------------------------------------------------
    finance_data = [
        [0.10, 35.0, -0.02, 0.20],
        [0.15, 42.0, -0.01, 0.18],
        [0.22, 55.0,  0.00, 0.21],
        [0.28, 63.0,  0.03, 0.25],
        [0.24, 58.0,  0.01, 0.23],
    ]

    result = client.run_any(
        data=finance_data,
        mode="FINANCE",
        label="finance_demo_window",
        metadata={
            "symbol": "TSLA",
            "note": "synthetic feature window – replace with real indicators",
        },
    )

    print("=== TQNN AnyEngine FINANCE demo ===")
    print("Mode:      ", result.get("mode"))
    print("Label:     ", result.get("label"))
    print("Probs:     ", result.get("probs"))
    print("Threshold: ", result.get("threshold"))
    print("Qualia:    ", result.get("qualia"))
    print("Intent:    ", result.get("intent"))
    print("Usage:     ", result.get("usage"))


if __name__ == "__main__":
    main()