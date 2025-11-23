TQNN AnyEngine API

Public SaaS API for TQNN AnyEngine
Modes: EEG / Finance / Tabular / Image / Any-Data


---

Overview

TQNN — Tubulin Quantum Neural Network is a quantum-inspired computational substrate.
It transforms incoming data into quantum-state inference embeddings using spiral entanglement and GHZ cobordism models.

Unlike classical ML:

There are no train/fit loops

There are no gradients

There are no weights to tweak


You send structured data → the substrate returns:

inference probabilities

threshold / tau

qualia embedding

intent vector

decision geometry


This repository provides only the public API wrapper and examples.
It does not include the TQNN Core substrate logic.


---

Modes Supported

EEG

Input: (channels x samples) numerical matrix
Output: brain-state basins, coherence bins, intent vectors

Tabular

Input: sample matrix
Output: class basin, phase threshold, decision quality

Finance

Input: OHLCV, indicators, rolling features
Output: directional probability, phase confidence, action geometry

Image (Beta)

Input: flattened or tensor image data
Output: perceptual probabilities, substrate embed vectors

Any structured numeric array can be used as input.


---

Authentication

Every customer receives a subscription-bound API key.
Send it using:

x-api-key: YOUR_TQNN_API_KEY

Quota is enforced at runtime.
Overages are billed automatically per request.


---

Client Installation

The official Python client will be distributed via PyPI:

pip install tqnn-client

Until then, use the provided tqnn_client.py.


---

Quickstart Example

Tabular request example:

from tqnn_client import TQNNClient
import os

BASE_URL = os.getenv("TQNN_API_URL", "https://YOUR-TQNN-ENDPOINT")
API_KEY  = os.getenv("TQNN_API_KEY", "YOUR_KEY")

client = TQNNClient(api_key=API_KEY, base_url=BASE_URL)

data = [
    [1.2, 0.4, 3.3, 0.1],
    [2.1, 1.1, 0.9, 0.5],
    [0.7, 0.3, 1.2, 2.1]
]

result = client.run_any(
    data=data,
    mode="TABULAR",
    label="demo_table"
)

print(result)


---

API Response Format

A typical inference response:

{
  "mode": "TABULAR",
  "label": "demo_table",
  "probs": [0.18, 0.44, 0.38],
  "threshold": 0.613,
  "qualia": "…",
  "intent": "…",
  "usage": 41
}

Notes:

threshold is a phase-space activation

qualia is a substrate embedding snapshot

intent is the decision geometry

usage increments with each call



---

Repository Contents

This repo includes:

API wrapper utilities

SDK client code

Request/response schema

Integration examples

Public demos


This repo does not include the Core substrate or any internal algorithms.


---

Licensing

This project is dual-licensed.

MIT License — Open Layer

The MIT license applies to:

API wrapper

Integration utilities

SDK client code

Example scripts

Public demos


You may freely:

Use

Modify

Integrate

Redistribute


See LICENSE.


---

Proprietary License — Core IP Locked

The following are closed-source and protected:

TQNN Core Engine

Tubulin substrate architecture

Spiral entanglement mesh

GHZ cobordism inference circuits

Qualia embedding and decision models

Internal runtime and training pipelines


These systems remain sealed.
Usage requires subscription tiers or an enterprise agreement.

See TQNN-Core-License.md.


---

Important Notice

This repository contains only the public API and client utilities.
It does not contain the substrate logic, inference systems, or internal algorithms.

Attempting to:

reverse-engineer,

extract embeddings to train competitors,

recreate GHZ logic,

reconstruct substrate mechanisms


is considered trade secret infringement.


---

Billing Model

Each API key has a monthly quota:

Tier	Monthly Requests	Intended Use

Tier 1	10,000	Builders / Research
Tier 2	50,000	Startups / Teams
Tier 3	200,000	Enterprise / Multi-modal


After quota exhaustion:

Requests continue

Per-unit billing applies

No engine code is exposed



---

Roadmap

PyPI client package

CLI tooling

Multi-modal SDK modules

Android edge inference

Enterprise substrate clusters

GPU acceleration for large input matrices



---

Contact

For enterprise licensing and integration:

tqnnlabs@gmail.com


---

Final Reminder

This repository provides:

The API surface

Client utilities

Usage examples


It does not provide:

The substrate

The inference algorithms

The architectural source


The Core remains sealed.


---