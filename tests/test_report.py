import unittest
from correlator.report import generate_markdown

class TestReport(unittest.TestCase):
    def test_generate_markdown_en(self):
        data = [
            {'cve': 'CVE-1234-5678', 'score': 2, 'sources': ['S1'], 'epss': 0.5, 'techniques': [{'id':'T1', 'name':'Tech 1'}], 'advisory_ids': []}
        ]
        md = generate_markdown(data, lang='en')
        self.assertIn("Threat Correlation Report", md)
        self.assertIn("CVE-1234-5678", md)
        self.assertIn("ATT&CK Techniques", md)

    def test_generate_markdown_nl(self):
        data = [
            {'cve': 'CVE-1234-5678', 'score': 2, 'sources': ['S1'], 'epss': 0.5, 'techniques': [], 'advisory_ids': []}
        ]
        md = generate_markdown(data, lang='nl')
        self.assertIn("Dreigingscorrelatierapport", md)
        self.assertIn("CVE ID: CVE-1234-5678", md)
        self.assertIn("EPSS Waarschijnlijkheid", md)

if __name__ == '__main__':
    unittest.main()
