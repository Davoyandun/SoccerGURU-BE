from typing import List

from core.src.repositories.soccer_api_repository import SoccerApiRepository
from core.src.use_cases.response import GetUpcomingMatchesResponse, UpcomingMatch


class GetUpcomingMatches:
    def __init__(self, soccer_repository: SoccerApiRepository):
        self.soccer_repository = soccer_repository


    def __map_upcoming_matches(self, data: List[dict]) -> List[UpcomingMatch]:
        matches = []
        for match in data:
            away_team_data: dict = match.get("teams")[0]
            home_team_data: dict = match.get("teams")[1]

            match_data = UpcomingMatch(
                away_team=away_team_data.get("displayName"),
                home_team=home_team_data.get("displayName"),
                id_away_team=away_team_data.get("id"),
                id_home_team=home_team_data.get("id"),
                logo_away_team=away_team_data.get("logo"),
                logo_home_team=home_team_data.get("logo"),
                date=match.get("date"),
            )
            matches.append(match_data)

        return matches


    def __call__(self):
        try:
            upcoming_matches = self.soccer_repository.get_upcoming_matches()
            upcoming_matches = self.__map_upcoming_matches(data=upcoming_matches)

            return GetUpcomingMatchesResponse(matches=upcoming_matches)
        except Exception as e:
            raise e
