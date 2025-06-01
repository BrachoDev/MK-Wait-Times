import requests
import pandas as pd
from datetime import datetime
import ast

# Magic Kingdom API URL from themeparks.wiki
API_URL = "https://api.themeparks.wiki/v1/entity/75ea578a-adc8-4116-a54d-dccb60765ef9/live"

# Fetching data from the API
response = requests.get(API_URL)
data = response.json()

# FUnction to Generate a CSV file with the live data
def generate_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"CSV file '{filename}' generated successfully.")


# Live data extraction
live_data = data["liveData"]

# Transforming the live data into a DataFrame
df = pd.DataFrame(live_data)

# Extract only the data where entityType = ATTRACTION
attractions = df[df["entityType"] == "ATTRACTION"]

# Looping through the attractions to extract relevant information
# initializing empty lists for rides and their details
rides = []
for attraction in attractions.itertuples():
    # Extracting the ride name
    ride_name = attraction.name

    # Extracting the status of the ride
    status = attraction.status

    # Extracting the ride queue information
    queue = attraction.queue

    # Extracting the ride wait time
    if isinstance(queue, dict):
        wait_time = queue.get('STANDBY', {}).get('waitTime', None)
    else:
        wait_time = None
    
    # Appending the ride details to the rides list
    rides.append({
        "ride_name": ride_name,
        "status": status,
        "wait_time": wait_time
    })


# Generating a CSV file with the rides data
generate_csv(rides, "Attractions_waitTimes.csv")