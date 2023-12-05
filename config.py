import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')
