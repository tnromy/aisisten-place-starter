import os
import requests
from dotenv import load_dotenv

# Load values from .env into environment variables
load_dotenv()

class GoogleMaps:
    @staticmethod
    def find_place(place_name):
        api_key = os.getenv("GOOGLE_API_KEY")
        endpoint = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"

        # Parameter untuk request
        params = {
            "input": place_name,
            "inputtype": "textquery",
            "key": api_key
        }

        # Header untuk request
        headers = {
            "Accept": "application/json"
        }

        # Mengirim GET request
        response = requests.get(endpoint, params=params, headers=headers)

        # Mengecek apakah request sukses (status code 200)
        if response.status_code == 200:
            # Parsing response JSON
            data = response.json()

            # Mendapatkan place_id dari candidates (jika ada)
            candidates = data.get("candidates", [])
            if candidates:
                place_id = candidates[0].get("place_id")
                return place_id
            else:
                print("Tidak ada candidates dalam response.")
                return False
        else:
            print("Request gagal dengan status code:", response.status_code)
            return False

    @staticmethod
    def getPlaceReviews(place_id):
        api_key = os.getenv("GOOGLE_API_KEY")
        endpoint = f"https://maps.googleapis.com/maps/api/place/details/json"

        # Parameter untuk request
        params = {
            "place_id": place_id,
            "language": "id",
            "key": api_key,
            "fields": "reviews"
        }

        # Header untuk request
        headers = {
            "Accept": "application/json"
        }

        # Mengirim GET request
        response = requests.get(endpoint, params=params, headers=headers)

        # Mengecek apakah request sukses (status code 200)
        if response.status_code == 200:
            # Parsing response JSON
            data = response.json()

            # Mendapatkan reviews dari response (jika ada)
            reviews = data.get("result", {}).get("reviews", [])
            return reviews
        else:
            print("Request gagal dengan status code:", response.status_code)
            return None

