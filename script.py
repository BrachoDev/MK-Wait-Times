import requests
import pandas as pd
from datetime import datetime

# Magic Kingdom API URL from themeparks.wiki
API_URL = "https://api.themeparks.wiki/v1/entity/75ea578a-adc8-4116-a54d-dccb60765ef9/live"

# Fetching data from the API
response = requests.get(API_URL)
data = response.json()

# printing the raw data for debugging in a json format
data = pd.json_normalize(data)