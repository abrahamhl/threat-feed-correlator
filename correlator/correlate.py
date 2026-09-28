from .normalize import extract_cves, extract_advisory_id

def merge_reports(feed_data):
    # feed_data is a list of dicts: {'source': 'feed_name', 'items': [{'title':..., 'description': ...}]}
    cve_map = {}
    
    for feed in feed_data:
        source = feed.get('source')
        for item in feed.get('items', []):
            text = f"{item.get('title', '')} {item.get('description', '')}"
            cves = extract_cves(text)
            adv_id = extract_advisory_id(text)
            
            if not cves and adv_id:
                cves = [f"ADV-{adv_id}"] # pseudo CVE if none
            
            for cve in cves:
                if cve not in cve_map:
                    cve_map[cve] = {
                        'cve': cve,
                        'sources': set(),
                        'titles': set(),
                        'advisory_ids': set(),
                        'score': 0
                    }
                cve_map[cve]['sources'].add(source)
                if item.get('title'):
                    cve_map[cve]['titles'].add(item.get('title').strip())
                if adv_id:
                    cve_map[cve]['advisory_ids'].add(adv_id)
                
    # Calculate score based on unique sources
    results = []
    for cve, data in cve_map.items():
        data['score'] = len(data['sources'])
        data['sources'] = list(data['sources'])
        data['titles'] = list(data['titles'])
        data['advisory_ids'] = list(data['advisory_ids'])
        results.append(data)
        
    return sorted(results, key=lambda x: x['score'], reverse=True)
