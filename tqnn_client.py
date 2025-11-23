"""
TQNN AnyEngine Python Client

Lightweight helper for calling the public TQNN AnyEngine API.

Usage:

    from tqnn_client import TQNNClient

    client = TQNNClient(
        api_key="YOUR_TQNN_API_KEY",
        base_url="https://YOUR-TQNN-ENDPOINT",  # no trailing slash
    )

    result = client.run_any(
        data=[[2, 3, 5, 7, 11, 13, 17, 1000, -5000, 333]],
        mode="TABULAR",
        label="chaos_test",
    )
    print(result)
"""

from typing import Any, Dict, List, Optional
import requests


class TQNNClient:
    """
    Minimal HTTP client for the TQNN AnyEngine SaaS API.
    """

    def __init__(self, api_key: str, base_url: str, timeout: int = 30):
        if not api_key:
            raise ValueError("api_key is required")
        if not base_url:
            raise ValueError("base_url is required")

        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    # ---- Core call ---------------------------------------------------------
    def run_any(
        self,
        data: Any,
        mode: str = "TABULAR",
        label: Optional[str] = None,
        sfreq: Optional[float] = None,
    ) -> Dict[str, Any]:
        """
        Call the /run/any endpoint.

        Args:
            data: Nested list / array-like.
            mode: "EEG", "FINANCE", "TABULAR", etc.
            label: Optional label or subject id.
            sfreq: Sampling frequency (required when mode == "EEG").

        Returns:
            Parsed JSON response from the TQNN API.
        """
        payload: Dict[str, Any] = {
            "data": data,
            "mode": mode,
            "label": label,
        }

        if mode.upper() == "EEG":
            if sfreq is None:
                raise ValueError("sfreq is required for EEG mode")
            payload["sfreq"] = float(sfreq)

        url = f"{self.base_url}/run/any"

        resp = requests.post(
            url,
            json=payload,
            headers={"x-api-key": self.api_key},
            timeout=self.timeout,
        )
        resp.raise_for_status()
        return resp.json()