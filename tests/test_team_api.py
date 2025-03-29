import unittest
from footyfetch.api import search_team_info

class TestTeamFetchAPI(unittest.TestCase):
    def test_big_team(self):
        # tests a big team like United or Real Madrid, etc
        team = search_team_info("Manchester United")
        self.assertIsNotNone(team)
        self.assertEqual(team["name"], "Manchester United")
        self.assertEqual(team["venue"], "Old Trafford")
        self.assertEqual(team["league"], "Premier League")

    def test_invalid_team(self):
        # tests any team that does not exist
        team = search_team_info("Tap In FC")
        self.assertIsNone(team)
    
    def test_case_insensitivity(self):
        # tests recognition with lowercase input
        team = search_team_info("real madrid")
        self.assertIsNotNone(team)
        self.assertEqual(team["name"], "Real Madrid")
        self.assertEqual(team["venue"], "Estadio Santiago Bernabéu")
        self.assertEqual(team["league"], "La Liga")

    def test_mls_team(self): # come  back to this
        team = search_team_info("Inter Miami")
        self.assertIsNotNone(team)
        self.assertEqual(team["name"], "Inter Miami")
        self.assertEqual(team["venue"], "Chase Stadium")

if __name__ == "__main__":
    unittest.main()