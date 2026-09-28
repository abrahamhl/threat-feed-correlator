# Threat Feed Correlator

![Tests Passing](https://img.shields.io/badge/tests-5%20passed-success)
![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

**Threat Feed Correlator** is an innovative OSINT tool built to cross-correlate multiple public Cyber Threat Intelligence (CTI) feeds (NCSC-NL, CERT-EU, BSI, CISA KEV) and produce a unified, deduplicated, and prioritized threat report. 

This project bridges the gap between scattered daily advisories and a real SOC workflow. By mapping CVEs to MITRE ATT&CK techniques and simulating EPSS probability enrichment, this tool replaces manual daily checking of multiple feeds for CTI analysts.

## Features

- **Cross-feed Correlation**: Automatically matches CVEs across different national and international feeds.
- **Scoring & Prioritization**: Higher correlation scores for vulnerabilities confirmed by multiple independent feeds.
- **MITRE ATT&CK Mapping**: Keyword-based extraction to map vulnerabilities to techniques.
- **Multilingual Reporting**: Generates Markdown reports in English, Dutch, and Spanish.
- **Zero Dependencies**: Pure Python 3 standard library implementation.

## Quick Start

```bash
# 1. Fetch latest advisories from public feeds
python -m correlator fetch

# 2. Correlate, deduplicate, and enrich
python -m correlator correlate

# 3. Generate a prioritized Markdown report (English, Dutch, or Spanish)
python -m correlator report --lang nl --out rapport.md
```

## Example Output

See [examples/sample-correlation-report.md](examples/sample-correlation-report.md) for a sample of the generated report.

## Scope & Limitations
- **Offline testing**: All unit tests run offline using fixtures and mocks to guarantee consistent CI/CD execution without external network dependency.
- **Live Feeds**: The `fetch` command requires an active internet connection to download from public RSS feeds (NCSC-NL, CERT-EU, etc.).
- **Not a SIEM Replacement**: This tool is designed for daily OSINT/CTI briefings and analyst augmentation, not for real-time log ingestion or alerting. 

## Testing

Run tests manually using:
```bash
python -m unittest discover tests
```
