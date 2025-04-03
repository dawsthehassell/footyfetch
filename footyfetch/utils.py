import json
import os
import time

CACHE_FILE = "cache.json"
CACHE_EXPIRY = 3600 

def load_cache():
    # Load cache data from file
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}   # Return empty dictionary if JSON is corrupted

def save_cache(cache_data):
    # Saves cache data to file
    with open(CACHE_FILE, "w") as f:
        json.dump(cache_data, f, indent=4)

def get_cached_data(key):
    # Retrieve data from cache if still valid (1 Hour)
    cache = load_cache()
    if key in cache:
        timestamp, data = cache[key]
        if time.time() - timestamp < CACHE_EXPIRY:
            return data
    return None     # Data is not cached or is expired

def set_cache_data(key, data):
    # Store data in cache with a timestamp
    cache = load_cache()
    cache[key] = (time.time(), data)
    save_cache(cache)

def clear_cache():
    if os.path.exists(CACHE_FILE):
        os.remove(CACHE_FILE)
        print("Cache file cleared.")
    else:
        print("No cache file found.")

MLS_teams = [
    "atlanta united",
    "austin fc",
    "charlotte fc",
    "chicago fire fc",
    "fc cincinnati",
    "colorado rapids",
    "columbus crew",
    "dc united",
    "fc dallas",
    "houston dynamo fc",
    "houston dynamo",
    "sporting kansas city",
    "la galaxy",
    "los angeles fc"
    "lafc",
    "inter miami cf",
    "inter miami",
    "minnesota united fc"
    "minnesota united",
    "cf montreal",
    "nashville sc",
    "new england revolution",
    "new york red bulls",
    "new york city fc",
    "orlando city",
    "philadelphia union",
    "portland timbers",
    "real salt lake",
    "san diego fc",
    "st louis city sc",
    "st louis city",
    "toronto fc",
    "toronto",
    "vancouver whitecaps fc",
    "vancouver whitecaps"
]   # stores MLS teams in case it's not recognized as MLS team thru the API