import os
from dotenv import load_dotenv
import requests

# Loads env variables from .env
load_dotenv()

# Gets API key from .env
API_KEY = os.getenv("API_FOOTBALL_KEY")
BASE_URL = "https://v3.football.api-sports.io/"

# Set global headers for API requests
HEADERS = {
    "x-apisports-key": API_KEY
}

def search_league_by_name(name):
    url = f"{BASE_URL}/leagues"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        leagues = response.json()["response"]
        for league_data in leagues:
            league = league_data["league"]
            if league["name"].lower() == name.lower():
                return league
        print(f"League '{name}' not found.")

    else:
        print(f"Error fetching leagues: {response.status_code} - {response.text}")
        
    return None
