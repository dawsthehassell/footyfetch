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

def search_league_by_name(league_name):
    url = f"{BASE_URL}/leagues"
    response = requests.get(url, headers=HEADERS)
    data = response.json()

    if "response" in data:
        leagues = data["response"] # list of leagues

        for league in leagues:
            league_info = league["league"]
            country_info = league.get("country", {}) # avoid KeyError if missing
            
            if league_name.lower() in league_info["name"].lower():
                return {
                    "name": league_info["name"],
                    "country": country_info.get("name", "unknown")
                }
        
    return None     # Return None if no match is found
