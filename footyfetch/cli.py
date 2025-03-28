import argparse
from footyfetch.api import search_league_by_name

def get_league_from_cli():
    # Handles CLI user input
    parser = argparse.ArgumentParser(description="FootyFetch, get realtime information about football")
    parser.add_argument("--league", type=str, help="Search for a league by name or country")
    args = parser.parse_args()

    if args.league:
        league = search_league_by_name(args.league)
        if league:
            print(f"Found league: {league['name']} ({league['country']})")
        else:
            print(f"League '{args.league}' not found. Try a different name.")