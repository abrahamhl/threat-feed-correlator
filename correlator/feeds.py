import urllib.request
import urllib.error
import json
import xml.etree.ElementTree as ET
import csv
import re
from datetime import datetime

def parse_rss(content):
    root = ET.fromstring(content)
    items = []
    for item in root.findall('.//item'):
        title = item.find('title').text if item.find('title') is not None else ''
        description = item.find('description').text if item.find('description') is not None else ''
        link = item.find('link').text if item.find('link') is not None else ''
        pubDate = item.find('pubDate').text if item.find('pubDate') is not None else ''
        items.append({
            'title': title,
            'description': description,
            'link': link,
            'pubDate': pubDate
        })
    return items

def fetch_feed(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None
