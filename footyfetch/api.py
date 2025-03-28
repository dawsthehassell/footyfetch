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
    url = f"{BASE_URL}leagues"
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

def search_team_info(team_name):
    url = f"{BASE_URL}teams"
    response = requests.get(url, headers=HEADERS, params={"search": team_name})
    data = response.json()

    if "response" in data and data["response"]:
        team_data = data["response"][0]
        team_id = team_data["team"]["id"]
        team_name = team_data["team"]["name"] # this variable name is also the input param
        team_venue = team_data["venue"]["name"]

        standings_url = f"{BASE_URL}standings"
        standings_response = requests.get(standings_url, headers=HEADERS, params={"team": team_id})
        standings_data = standings_response.json()

        if "response" in standings_data and standings_data["response"]:
            league_data = standings_data["response"][0]["league"]
            league_name = league_data["name"]
            standings = league_data["standings"][0][0]["rank"]

            return {
                "name": team_name,
                "venue": team_venue,
                "league": league_name,
                "standing": standings
            }
    
    return None     # Returns None if no team is found