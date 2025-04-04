import os
from dotenv import load_dotenv
import requests
from footyfetch.utils import get_cached_data, set_cache_data, MLS_teams

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
    cache_key = f"league_{league_name.lower()}"
    cached_data = get_cached_data(cache_key)

    if cached_data:
        return cached_data
    
    url = f"{BASE_URL}leagues"
    response = requests.get(url, headers=HEADERS)
    data = response.json()

    if "response" in data:
        leagues = data["response"]  # list of leagues

        for league in leagues:
            league_info = league["league"]
            country_info = league.get("country", {})  # avoid KeyError if missing
            
            if league_name.lower() in league_info["name"].lower():
                league_info = {
                    "name": league_info["name"],
                    "country": country_info.get("name", "unknown")
                }

                set_cache_data(cache_key, league_info)

                return league_info
        
    return None  # Return None if no match is found

def search_team_info(team_name):
    cache_key = f"team_{team_name.lower()}"
    cached_data = get_cached_data(cache_key)

    if cached_data:
        return cached_data
    
    url = f"{BASE_URL}teams"
    response = requests.get(url, headers=HEADERS, params={"search": team_name})
    data = response.json()

    if data.get("response") and isinstance(data["response"], list) and len(data["response"]) > 0:
        best_match = None
        for team in data["response"]:
            team_name_api = team["team"]["name"]
            if team_name.lower() == team_name_api.lower():
                best_match = team
                break
            if best_match is None and team_name.lower() in team_name_api.lower():
                best_match = team

        team_data = best_match if best_match else data["response"][0]
        team_id = team_data["team"]["id"]
        team_name_api = team_data["team"]["name"]
        team_venue = team_data["venue"]["name"]
        season = 2023  # adjust to be dynamic?

        leagues_url = f"{BASE_URL}leagues"
        leagues_response = requests.get(leagues_url, headers=HEADERS, params={"team": team_id})
        leagues_data = leagues_response.json()

        league_id = None
        league_name = "Unknown League"  # Initialize `league_name` here

        for league_entry in leagues_data.get("response", []):
            league = league_entry["league"]
            if league["name"] == "Major League Soccer":
                league_id = league["id"]
                league_name = "Major League Soccer"
                break

        if league_id is None and leagues_data.get("response"):
            first_league = leagues_data["response"][0]["league"]
            league_id = first_league.get("id")
            league_name = first_league.get("name", "Unknown League")
        
        if not league_id:
            league_name = "N/A"
            standings = "N/A"
        else:
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
            else:
                standings = "N/A"

        team_info = {
            "name": team_name_api,
            "venue": team_venue,
            "league": league_name,
            "standing": standings
        }

        set_cache_data(cache_key, team_info)
        
        return team_info
        
    return None

