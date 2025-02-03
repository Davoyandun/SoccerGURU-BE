from typing import NamedTuple, List, Optional


class UpcomingMatch(NamedTuple):
    date: Optional[str]
    home_team: Optional[str]
    away_team: Optional[str]
    id_home_team: Optional[int]
    id_away_team: Optional[int]
    logo_home_team: Optional[str]
    logo_away_team: Optional[str]


class GetUpcomingMatchesResponse(NamedTuple):
    matches: List[UpcomingMatch]
