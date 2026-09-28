# Threat Feed Correlator

![Tests Passing](https://img.shields.io/badge/tests-7%20passed-success)
![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Dependencies](https://img.shields.io/badge/dependencies-0-success)

Cyber threat analysts spend hours manually checking disparate national CERT feeds to identify vulnerabilities being actively targeted. **Threat Feed Correlator** automates this by cross-referencing public advisories, mapping them to EPSS probability, and generating a unified, deduplicated daily briefing.

## What it correlates

| Feed | What it gives | Format |
|---|---|---|
| **NCSC-NL** | Dutch national cyber security advisories | RSS |
| **CERT-EU** | European Union institutional advisories | RSS / JSON |
| **BSI** | German Federal Office for Information Security | RSS |
| **CISA KEV** | Known Exploited Vulnerabilities catalog | JSON |
| **EPSS** | Exploit Prediction Scoring System probabilities | API (CSV/JSON) |

## How correlation works

The system fetches the latest advisories from the configured feeds and normalizes them into a standard internal format. It then groups them by CVE ID, scoring the vulnerability based on how many independent CERTs have issued an advisory for it. Finally, it enriches the prioritized list with CISA KEV status and EPSS scores to help analysts focus on what matters most.

## Quick Start

```bash
# 1. Fetch latest advisories from public feeds
python -m correlator fetch

# 2. Correlate, deduplicate, and enrich
python -m correlator correlate

# 3. Generate a prioritized Markdown report
python -m correlator report --out report.md
```

## Example Output

See [examples/sample-correlation-report.md](examples/sample-correlation-report.md) for a sample of the generated report.

## Scope & Limitations

- **Offline testing**: All unit tests run offline using static fixtures.
- **Live Feeds**: The `fetch` command requires an active internet connection to download from public RSS feeds.
- **Educational / Workflow Tool**: This is a standalone Python CLI tool for automating OSINT collection, not a real-time SIEM or enterprise threat intelligence platform.
