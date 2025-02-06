from typing import List
import requests
from datetime import datetime
from zoneinfo import ZoneInfo

from core.src.repositories import SoccerApiRepository
from config.constants import UEFA_RAPID_API_URL, X_RAPID_API_HOST
from config.env_variables import X_RAPID_API_KEY
import requests
import os
from datetime import datetime

from core.src.repositories import SoccerApiRepository
from .services import RapidAPIService


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
        
    
    rapidapi = RapidAPIService(url="https://uefa-champions-league1.p.rapidapi.com")


    def get_statistics(self, team_id_1: int, team_id_2: int):
        try:
            endpoint = "/team/statistic/scoring"
            current_season = datetime.now().year - 2
            seasons_to_search = [current_season - 2, current_season - 3]
            teams_id = [team_id_1, team_id_2]
            results = {team_id_1: {}, team_id_2: {}}
            print(seasons_to_search)
            print(teams_id)

            for season in seasons_to_search:
                for team_id in teams_id:
                    query = {"season": str(season), "teamId": str(team_id)}
                    print("[DEBUG] Query: ", query)
                    results_team = self.rapidapi(endpoint=endpoint, querystring=query)

                    if results_team["status"] == "success":
                        results[team_id][season] = results_team
                    else:
                        results[team_id][season] = {"status": "Not found"}

                    print("[DEBUG] Results team 1: ", results_team)
                    # if not results_team["error"]:
                    #     print("into if")
                    #     results[team_id_1][season] = results_team

                    # else:
                    #     print("into else")
                    #     results[team_id][season] = {"status": "Not found"}
            print("[DEBUG] Results: ", results)
            return results

            # for season in seasons_to_search:
            #     print("[DEBUG] Season: ", season)
            #     print("[DEBUG] Team 1: ", team_id_1)
            #     print("[DEBUG] Team 2: ", team_id_2)
            #     querystring1 = {"season": season, "teamId": team_id_1}
            #     results_team_1 = self.rapidapi(
            #         endpoint=endpoint, querystring=querystring1
            #     )

            #     querystring2 = {"season": season, "teamId": team_id_2}
            #     results_team_2 = self.rapidapi(
            #         endpoint=endpoint, querystring=querystring2
            #     )

            #     if results_team_1["error"]:
            #         results_team_1 = {"status": "Not found"}
            #         print("into if t1")

            #     elif results_team_2["error"]:
            #         results_team_2 = {"status": "Not found"}
            #         print("into if t2")

            #     print("into else t1")

            # results_data = results_team_1.get("results")
            # #print("[DEBUG] Results data ELSE: ", results_data)
            # if len(results_data) > 0:
            #     for key, value in results_data.items():
            #         results_data[team_id_1][season] = (
            #             __get_total_and_individual_results(results=results_data)
            #         )
            # else:
            #     results_data[team_id_1][season] = {"status": "Not found"}
            # results_data = results_team_2.get("results").get("stats")
            # if len(results_data) > 0:
            #     for key, value in results_data.items():
            #         results_data[team_id_2][season] = (
            #             __get_total_and_individual_results(results=results_data)
            #         )
            # else:
            #     results_data[team_id_2][season] = {"status": "Not found"}

            # else:
            #     print("into else t1")
            #     results_data = results_team_1.get("results")
            #     print("[DEBUG] Results data: ", results_data)
            #     if len(results_data) > 0:
            #         for key, value in results_data.items():
            #             results_data[team_id_1][season] = (
            #                 __get_total_and_individual_results(results=results_data)
            #             )
            #     else:
            #         results_data[team_id_1][season] = {"status": "Not found"}

            # querystring = {"season": season, "teamId": team_id_2}
            # results_team_2 = self.rapidapi(
            #     endpoint=endpoint, querystring=querystring
            # )
            # if results_team_2["error"]:
            #     results_team_2 = {"status": "Not found"}

            # else:
            #     results_data = results_team_2.get("results").get("stats")
            #     if len(results_data) > 0:
            #         for key, value in results_data.items():
            #             results_data[team_id_2][season] = (
            #                 __get_total_and_individual_results(results=results_data)
            #             )
            #     else:
            #         results_data[team_id_2][season] = {"status": "Not found"}

            # print("[DEBUG] Results team 1: ", results_team_1)
            # print("[DEBUG] Results team 2: ", results_team_2)
            # results[season] = {"team_1": results_team_1, "team_2": results_team_2}
            # results[team_id_1] = self.rapidapi(
            #     endpoint=endpoint, querystring=querystring
            # )
            # querystring = {"season": season, "teamId": team_id_2}
            # results[team_id_2] = self.rapidapi(
            #     endpoint=endpoint, querystring=querystring
            # )

            # results = self.rapidapi(endpoint=endpoint, querystring={"teamId": team_id_1})
            # results_team_1 = self.rapidapi(endpoint=endpoint, querystring={"teamId": str(team_id_1), "season": str(current_season)})
            # results_team_2 = self.rapidapi(endpoint=endpoint, querystring={"teamId": str(team_id_2), "season": str(current_season)})
            # print("[DEBUG] Results: ", results)
            # return results

        except Exception as e:
            raise

    def __get_total_and_individual_results(results: dict):
        total_stats = 0
        parsed_results = {}
        stat = results.get("results").get("name")
        full_individual_stats = results.get("leaders")

        for key, value in full_individual_stats.items():
            total_stats += value.get("value")
            player = value.get("athlete").get("displayName")
            parsed_results[player] = value.get("value")

        parsed_results[stat] = total_stats

        return parsed_results
