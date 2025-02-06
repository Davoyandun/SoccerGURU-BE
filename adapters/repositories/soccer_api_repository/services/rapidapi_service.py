import os
import requests
from dotenv import load_dotenv

load_dotenv()


class RapidAPIService:
    def __init__(self, url: str):
        self.base_url = url
        self.headers = {
            "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
            "x-rapidapi-host": os.getenv("RAPIDAPI_HOST"),
        }

    def __call__(self, endpoint: str, querystring: dict):
        full_url = self.base_url + endpoint
        try:
            response = requests.get(
                url=full_url, headers=self.headers, params=querystring
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            return {"error": str(err)}
        except Exception as err:
            return {"error": str(err)}
