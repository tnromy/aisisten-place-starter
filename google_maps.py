import os
from dotenv import load_dotenv

# Load values from .env into environment variables
load_dotenv()

# Access environment variables
class GoogleMaps:
	def findPlace():
		api_key = os.getenv("GOOGLE_API_KEY")
		print(api_key)

GoogleMaps.findPlace()