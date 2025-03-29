import argparse
from footyfetch.api import search_league_by_name, search_team_info

def get_info_from_cli():
    # Handles CLI user input
    parser = argparse.ArgumentParser(description="FootyFetch, get realtime information about football")
    parser.add_argument("--league", type=str, help="Search for a league by name or country")
    parser.add_argument("--team", type=str, help="Search for a team by name")
    args = parser.parse_args()

    if args.league:
        league = search_league_by_name(args.league)
        if league:
            print(f"Found league: {league['name']} ({league['country']})")
        else:
            print(f"League '{args.league}' not found. Try a different name.")
    
    if args.team:
        team = search_team_info(args.team)

        if team:
            print(f"Team: {team['name']}")
            print(f"Stadium: {team['venue']}")
            print(f"Domestic League: {team['league']}")
            if team['standing'] != "N/A":
                print(f"23-24 League Place: {team['standing']} place")
            else:
                print(f"23-24 League Place: Unavailable")
        else:
            print(f"Team '{args.team}' not found. Try a different name.")
