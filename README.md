# Air Quality ETL Process  

This repository contains a simple Python script (AirQuality_ETL.py) for extracting, transforming, and loading (ETL) air quality data from a specified location using the RapidAPI service. The extracted data is then transformed into a Pandas DataFrame and saved as a CSV file for further analysis.

## Getting Started  

To use this script, follow the steps below:

### Prerequisites  
**RapidAPI Key:** Obtain your RapidAPI key and update the .env file with your key. If you don't have a key, sign up on the RapidAPI website and create a new project to obtain your API key.

**Dependencies:** Install the required Python libraries by running the following command:



bash
Copy code
pip install -r requirements.txt  

### Usage  

Run the AirQuality_ETL.py script:

bash
Copy code
python AirQuality_ETL.py
Check the generated air_quality_data.csv file for the extracted air quality data in CSV format.

### Project Structure  

**AirQuality_ETL.py:** Python script for ETL process.
**config.py:** Configuration file containing the RapidAPI key.
**.env:** Environment file storing sensitive information (e.g., API keys).
**requirements.txt:** List of Python dependencies.  

### Configuration  

Ensure that you have updated the .env file with your RapidAPI key:

env
Copy code
RAPIDAPI_KEY="your_rapidapi_key_here"