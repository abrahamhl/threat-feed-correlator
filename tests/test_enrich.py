import unittest
import os
import json
from correlator.enrich import map_attack_techniques, load_attack_techniques

class TestEnrich(unittest.TestCase):
    def setUp(self):
        # Create a mock attack_techniques.json in data folder
        pass

    def test_map_attack_techniques(self):
        res = map_attack_techniques("This is a Remote Code Execution vulnerability.")
        ids = [r['id'] for r in res]
        self.assertIn("T1190", ids)

if __name__ == '__main__':
    unittest.main()
