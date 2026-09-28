def deduplicate(correlated_data):
    deduped = []
    seen_adv = set()
    for item in correlated_data:
        skip = False
        for adv in item.get('advisory_ids', []):
            if adv in seen_adv:
                skip = True
            seen_adv.add(adv)
        if not skip:
            deduped.append(item)
    return deduped
