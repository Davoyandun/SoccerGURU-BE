from typing import NamedTuple, List


class UpcomingMatch(NamedTuple):
    date: str
    home_team: str
    away_team: str
    id_home_team: int
    id_away_team: int
    logo_home_team: str
    logo_away_team: str


class GetUpcomingMatchesResponse(NamedTuple):
    matches: List[UpcomingMatch]
