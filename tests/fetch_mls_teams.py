import requests
import os
from dotenv import load_dotenv
# Loads env variables from .env
load_dotenv()

# Gets API key from .env
API_KEY = os.getenv("API_FOOTBALL_KEY")
BASE_URL = "https://v3.football.api-sports.io/"

HEADERS = HEADERS = {
    "x-apisports-key": API_KEY
}

def fetch_league_teams(league_id, season=2023):
    url = f"{BASE_URL}teams"
    response = requests.get(url, headers=HEADERS, params={"league": league_id, "season": season})
    return response.json()

mls_teams = fetch_league_teams(253)
print(mls_teams)