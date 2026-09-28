import unittest
from correlator.normalize import extract_cves, extract_advisory_id

class TestNormalize(unittest.TestCase):
    def test_extract_cves(self):
        text = "Vulnerability in system, tracked as CVE-2023-12345 and CVE-2021-9876."
        cves = extract_cves(text)
        self.assertIn("CVE-2023-12345", cves)
        self.assertIn("CVE-2021-9876", cves)

    def test_extract_advisory_id(self):
        self.assertEqual(extract_advisory_id("NCSC-NL-2024-0001"), "NCSC-NL-2024-0001")
        self.assertEqual(extract_advisory_id("CERT-EU-2023-010"), "CERT-EU-2023-010")

if __name__ == '__main__':
    unittest.main()
