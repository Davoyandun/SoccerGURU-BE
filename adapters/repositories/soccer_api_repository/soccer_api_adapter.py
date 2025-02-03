from typing import List
import requests
from datetime import datetime
from zoneinfo import ZoneInfo

from core.src.repositories import SoccerApiRepository
from config.constants import UEFA_RAPID_API_URL, X_RAPID_API_HOST
from config.env_variables import X_RAPID_API_KEY


class UEFAChampionsLeagueApiAdapter(SoccerApiRepository):

    def __get_non_empty_list(self, data: dict) -> List[dict]:
        for key, value in data.items():
            if isinstance(value, list) and value:
                return value
        return None


    def get_upcoming_matches(self):
        try:
            url = f"{UEFA_RAPID_API_URL}/schedule"
            current_year = datetime.now().year
            current_month = datetime.now().month
            querystring = {"year": current_year, "month": current_month}
            headers = {
                "x-rapidapi-key": X_RAPID_API_KEY,
                "x-rapidapi-host": X_RAPID_API_HOST
            }

            response = requests.get(url, headers=headers, params=querystring)

            data = response.json()
            upcoming_matches_data = data["schedule"]
            upcoming_matches_data = self.__get_non_empty_list(upcoming_matches_data)
        
            return upcoming_matches_data
        except Exception as e:
            raise e
        
    
    def get_statistics(self, team_id_1: int, team_id_2: int):
        raise NotImplementedError
