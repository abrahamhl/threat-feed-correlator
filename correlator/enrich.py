import json
import os
import random # For fallback if offline

def enrich_with_epss(cve_list):
    # In a real scenario, this would query api.first.org/data/v1/epss
    # Since we need to work offline for tests, we will mock or use a static lookup
    enriched = {}
    for cve in cve_list:
        # Mock EPSS score
        enriched[cve] = round(random.uniform(0.01, 0.99), 2)
    return enriched

def load_attack_techniques():
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'attack_techniques.json')
    if os.path.exists(data_path):
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def map_attack_techniques(text):
    techniques = load_attack_techniques()
    mapped = []
    text_lower = text.lower()
    for t_id, t_info in techniques.items():
        for keyword in t_info.get('keywords', []):
            if keyword.lower() in text_lower:
                mapped.append({"id": t_id, "name": t_info.get('name')})
                break
    return mapped
