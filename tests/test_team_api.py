import unittest
from footyfetch.api import search_team_info

class TestTeamFetchAPI(unittest.TestCase):
    def test_english_team(self):
        # tests a big team like United or Real Madrid, etc
        team = search_team_info("Manchester United")
        self.assertIsNotNone(team)
        self.assertEqual(team["name"], "Manchester United")
        self.assertEqual(team["venue"], "Old Trafford")
        self.assertEqual(team["league"], "Premier League")

    def test_bundesliga_team(self):
        team = search_team_info("Borussia Dortmund")
        self.assertIsNotNone(team)
        self.assertEqual(team["name"], "Borussia Dortmund")
        self.assertEqual(team["venue"], "BVB Stadion Dortmund")
        self.assertEqual(team["league"], "Bundesliga")

    def test_serie_a_team(self):
        team = search_team_info("Udinese Calcio")
        self.assertIsNotNone(team)
        self.assertEqual(team["name"], "Udinese Calcio")
        self.assertEqual(team["venue"], "Stadio Friuli")
        self.assertEqual(team["league"], "Serie A")

    def test_la_liga_team(self):
        team = search_team_info("RCD Espanyol")
        self.assertIsNotNone(team)
        self.assertEqual(team["name"], "RCD Espanyol de Barcelona")
        # another test for another version of their name? "RCD Espanyol" or "Espanyol"
        self.assertEqual(team["venue"], "RCDE Stadium")
        self.assertEqual(team["league"], "La Liga")

    def test_dutch_team(self):
        team = search_team_info("Feyenoord")
        self.assertIsNotNone(team)
        self.assertEqual(team["name"], "Feyenoord")
        self.assertEqual(team["venue"], "Stadion Feijenoord")
        self.assertEqual(team["league"], "Eredivisie")

    def test_saudi_team(self):
        team = search_team_info("Al-Nassr")
        self.assertIsNotNone(team)
        self.assertEqual(team["name"], "Al-Nassr")
        self.assertEqual(team["venue"], "Al-Awwal Park") # they have a second stadium "Prince Faisal Bin Fahd Stadium"
        self.assertEqual(team["league"], "Saudi Pro League") # also called Roshn Saudi League

    def test_mexican_team(self):
        team = search_team_info("Club America")
        self.assertIsNotNone(team)
        self.assertEqual(team["name"], "Club America") # Club de Futbol America S.A. de C.V.
        self.assertEqual(team["venue"], "Estadio Azteca") # or Estadio Cuidad de los Deportes
        self.assertEqual(team["league"], "Liga MX")

    def test_french_league(self):
        team = search_team_info("Paris Saint Germain")
        self.assertIsNotNone(team)
        self.assertEqual(team["name"], "Paris Saint-Germain")
        self.assertEqual(team["venue"], "Parc des Princes")
        self.assertEqual(team["league"], "Ligue 1")

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

if __name__ == "__main__":
    unittest.main()