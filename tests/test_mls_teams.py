import unittest
from footyfetch.api import search_team_info
from footyfetch.utils import MLS_teams

class TestMLSTeams(unittest.TestCase):

    def test_mls_team_identification(self):
        self.assertIn("Vancouver Whitecaps".lower(), MLS_teams)

    def test_mls_team_league_and_standings(self):
        result = search_team_info("Vancouver Whitecaps")
        self.assertIsNotNone(result)
        self.assertEqual(result["league"], "MLS")
        self.assertEqual(result["standing"], "Unavailable")
    
    def test_non_mls_team(self):
        result = search_team_info("Arsenal")
        self.assertIsNotNone(result)
        self.assertNotEqual(result["league"], "MLS")
        self.assertNotEqual(result["standing"], "Unavailable")

if __name__ == "__main__":
    unittest.main()