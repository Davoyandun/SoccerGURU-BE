from typing import List

from core.src.repositories import SoccerApiRepository
from datetime import datetime

from core.src.repositories import SoccerApiRepository
from .services import RapidAPIService
from config import STAT_TYPES

class UEFAChampionsLeagueApiAdapter(SoccerApiRepository):

    rapidapi = RapidAPIService(url="https://uefa-champions-league1.p.rapidapi.com")


    def __get_non_empty_list(self, data: dict) -> List[dict]:
        for key, value in data.items():
            if isinstance(value, list) and value:
                return value
        return None
    

    def __total_stat_value(self, stats: List[dict]) -> int:
        total = 0
        for stat in stats:
            total += stat["value"]

        return total


    def get_upcoming_matches(self):
        try:
            current_year = datetime.now().year
            current_month = datetime.now().month
            querystring = {"year": current_year, "month": current_month}

            response = self.rapidapi(endpoint="/schedule", querystring=querystring)

            upcoming_matches_data = response["schedule"]
            upcoming_matches_data = self.__get_non_empty_list(upcoming_matches_data)
        
            return upcoming_matches_data
        except Exception as e:
            raise e


    def get_statistics(self, team_id_1: str, team_id_2: str):
        try:
            endpoint = "/team/statistic/scoring"
            results = {team_id_1: {}, team_id_2: {}}

            for team_id in [team_id_1, team_id_2]:
                query = {"teamId": team_id} 
                response = self.rapidapi(endpoint=endpoint, querystring=query)
                if response["status"] == "success":
                    results_team = response["results"]
                    team_name = response["team"]["name"]
                    stats = results_team["stats"]
                    results[team_id]["name"] = team_name

                    if len(stats) > 0:
                        for stat in stats:
                            if stat["name"] in STAT_TYPES:
                                total_current_stat = self.__total_stat_value(stat["leaders"])
                                results[team_id][stat["name"]] = total_current_stat
                    else:
                        results[team_id] = {"stats": "Not found"}
                else:
                    results[team_id] = {"status": "Not found"}

            return results
        except Exception as e:
            raise e
