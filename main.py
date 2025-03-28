from footyfetch.api import get_leagues  # Import the function

leagues = get_leagues()  # Call the function

if leagues:
    print("✅ API request successful!")
    print(leagues)  # Print the raw JSON response
else:
    print("❌ API request failed.")