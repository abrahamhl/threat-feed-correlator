import re

def extract_cves(text):
    if not text:
        return []
    cve_pattern = re.compile(r'CVE-\d{4}-\d{4,7}')
    return list(set(cve_pattern.findall(text)))

def normalize_cve(cve_str):
    return cve_str.upper().strip()

def extract_advisory_id(text):
    # Simplistic extraction for testing purposes
    match = re.search(r'(NCSC-NL-\d{4}-\d+|CERT-EU-\d{4}-\d+)', text)
    if match:
        return match.group(0)
    return None
