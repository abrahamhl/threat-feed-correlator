import unittest
from correlator.correlate import merge_reports

class TestCorrelate(unittest.TestCase):
    def test_merge_reports(self):
        feed_data = [
            {"source": "S1", "items": [{"title": "Vuln CVE-2023-1000", "description": ""}]},
            {"source": "S2", "items": [{"title": "Bug CVE-2023-1000", "description": ""}]},
            {"source": "S3", "items": [{"title": "CVE-2023-1000 RCE", "description": ""}]}
        ]
        res = merge_reports(feed_data)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]['cve'], 'CVE-2023-1000')
        self.assertEqual(res[0]['score'], 3)
        self.assertEqual(len(res[0]['sources']), 3)

if __name__ == '__main__':
    unittest.main()
