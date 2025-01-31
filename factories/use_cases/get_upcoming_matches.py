from core.src.use_cases.get_upcoming_matches import GetUpcomingMatches
from factories.repositories import soccer_api_repository

def get_upcoming_matches_use_case() -> GetUpcomingMatches:
    return GetUpcomingMatches(soccer_repository=soccer_api_repository())
