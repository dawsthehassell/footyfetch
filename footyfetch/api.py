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
    response = requests.get(url, headers=HEADERS, params={"search": {team_name}})
    data = response.json()

    if data.get("response") and isinstance(data["response"], list) and len(data["response"]) > 0:
        team_data = data["response"][0]
        team_id = team_data["team"]["id"]
        team_name_api = team_data["team"]["name"]
        team_venue = team_data["venue"]["name"]
        season = 2023 # adjust to be dynamic?

        leagues_url = f"{BASE_URL}leagues"
        leagues_response = requests.get(leagues_url, headers=HEADERS, params={"team": team_id})
        leagues_data = leagues_response.json()

        if "response" in leagues_data and leagues_data["response"]:
            league_data = leagues_data["response"][0]["league"]
            league_id = league_data.get("id")
            league_name = league_data.get("name", "Unknown League")
        else:
            print("ERROR: No league data found for team!")
            return None
        
        if isinstance(league_id, int): # ensures league id is an int
            standings_url = f"{BASE_URL}standings"
            standings_response = requests.get(standings_url, headers=HEADERS, params={
                "team": team_id,
                "league": league_id,
                "season": season
                })
            standings_data = standings_response.json()

            if "response" in standings_data and standings_data["response"]:
                standings_list = standings_data["response"][0]["league"]["standings"]
                
                if isinstance(standings_list, list) and len(standings_list) > 0:
                    standings = standings_list[0][0]["rank"]
                else:
                    standings = "N/A"

            return {
                "name": team_name_api,
                "venue": team_venue,
                "league": league_name,
                "standing": standings
            }
        
        return None     # Returns None if no team is found