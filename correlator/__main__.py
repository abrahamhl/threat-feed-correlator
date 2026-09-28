import argparse
import sys
import json
from .feeds import fetch_feed, parse_rss
from .correlate import merge_reports
from .dedup import deduplicate
from .enrich import enrich_with_epss, map_attack_techniques
from .report import generate_markdown

def main():
    parser = argparse.ArgumentParser(description="Threat Feed Correlator")
    subparsers = parser.add_subparsers(dest="command")

    # fetch
    fetch_parser = subparsers.add_parser("fetch")

    # correlate
    correlate_parser = subparsers.add_parser("correlate")
    correlate_parser.add_argument("--data", help="Path to feed data JSON", default="feeds_data.json")

    # report
    report_parser = subparsers.add_parser("report")
    report_parser.add_argument("--lang", choices=["en", "nl", "es"], default="en")
    report_parser.add_argument("--out", required=True)
    report_parser.add_argument("--data", help="Path to correlated data JSON", default="correlated_data.json")

    args = parser.parse_args()

    if args.command == "fetch":
        urls = {
            "NCSC-NL": "https://advisories.ncsc.nl/rss/advisories",
            "CERT-EU": "https://cert.europa.eu/api/v1/publish/rss/advisories"
        }
        feed_data = []
        for name, url in urls.items():
            content = fetch_feed(url)
            if content:
                items = parse_rss(content)
                feed_data.append({"source": name, "items": items})
        with open("feeds_data.json", "w", encoding="utf-8") as f:
            json.dump(feed_data, f, indent=2)
        print("Fetched feeds saved to feeds_data.json")

    elif args.command == "correlate":
        try:
            with open(args.data, "r", encoding="utf-8") as f:
                feed_data = json.load(f)
        except FileNotFoundError:
            print("Run fetch first or provide --data")
            sys.exit(1)
            
        correlated = merge_reports(feed_data)
        deduped = deduplicate(correlated)
        
        cves = [item['cve'] for item in deduped]
        epss_scores = enrich_with_epss(cves)
        
        for item in deduped:
            item['epss'] = epss_scores.get(item['cve'])
            combined_text = " ".join(item['titles'])
            item['techniques'] = map_attack_techniques(combined_text)
            
        with open("correlated_data.json", "w", encoding="utf-8") as f:
            json.dump(deduped, f, indent=2)
        print("Correlated data saved to correlated_data.json")

    elif args.command == "report":
        try:
            with open(args.data, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("Run correlate first or provide --data")
            sys.exit(1)
            
        md = generate_markdown(data, lang=args.lang)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Report generated: {args.out}")

if __name__ == "__main__":
    main()
