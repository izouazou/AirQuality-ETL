# Importing necessary libraries
import requests  # Library for making HTTP requests
from config import Config  # Config contains the API key
import pandas as pd  # Library for data manipulation and analysis

# API endpoint URL for air quality data
url = "https://air-quality.p.rapidapi.com/history/airquality"

# Query parameters for a specific location (latitude and longitude)
querystring = {"lon": "-78.638", "lat": "35.779"}

# Headers including the RapidAPI key for authentication
headers = {
    "X-RapidAPI-Key": Config.RAPIDAPI_KEY,
    "X-RapidAPI-Host": "air-quality.p.rapidapi.com"
}

# Extract

# Making a GET request to the API to extract data
response = requests.get(url, headers=headers, params=querystring)

# Printing the JSON response from the API for inspection
print(response.json())

# Extracting data from the JSON response
data = response.json()

# Transform

# Extracting air quality data from the API response
air_quality_data = data.get('data', [])

# Creating a DataFrame from the extracted data
df = pd.DataFrame(air_quality_data)

# Load

# Saving the DataFrame to a CSV file
df.to_csv('air_quality_data.csv', index=False)

# Printing the DataFrame for verification or further inspection
print(df)