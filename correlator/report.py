import json

TRANSLATIONS = {
    'en': {
        'title': 'Threat Correlation Report',
        'cve': 'CVE ID',
        'score': 'Correlation Score',
        'sources': 'Sources',
        'techniques': 'ATT&CK Techniques',
        'epss': 'EPSS Probability'
    },
    'nl': {
        'title': 'Dreigingscorrelatierapport',
        'cve': 'CVE ID',
        'score': 'Correlatiescore',
        'sources': 'Bronnen',
        'techniques': 'ATT&CK Technieken',
        'epss': 'EPSS Waarschijnlijkheid'
    },
    'es': {
        'title': 'Informe de Correlación de Amenazas',
        'cve': 'ID de CVE',
        'score': 'Puntuación de Correlación',
        'sources': 'Fuentes',
        'techniques': 'Técnicas ATT&CK',
        'epss': 'Probabilidad EPSS'
    }
}

def generate_markdown(data, lang='en'):
    t = TRANSLATIONS.get(lang, TRANSLATIONS['en'])
    lines = [f"# {t['title']}\n"]
    
    for item in data:
        lines.append(f"## {t['cve']}: {item['cve']} (Score: {item['score']})")
        lines.append(f"**{t['epss']}**: {item.get('epss', 'N/A')}")
        lines.append(f"**{t['sources']}**: {', '.join(item['sources'])}")
        if item.get('advisory_ids'):
            lines.append(f"**Advisories**: {', '.join(item['advisory_ids'])}")
        if item.get('techniques'):
            techs = [f"{tech['id']} ({tech['name']})" for tech in item['techniques']]
            lines.append(f"**{t['techniques']}**: {', '.join(techs)}")
        
        lines.append("\n### Titles")
        for title in item.get('titles', []):
            lines.append(f"- {title}")
        lines.append("\n---\n")
        
    return '\n'.join(lines)
