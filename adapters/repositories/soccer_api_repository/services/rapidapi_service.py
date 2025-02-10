import requests
from config.constants import X_RAPID_API_HOST
from config.env_variables import X_RAPID_API_KEY


class RapidAPIService:
    def __init__(self, url: str):
        self.base_url = url
        self.headers = {
            "x-rapidapi-key": X_RAPID_API_KEY,
            "x-rapidapi-host": X_RAPID_API_HOST,
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
