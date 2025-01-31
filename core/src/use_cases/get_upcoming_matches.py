from core.src.repositories.soccer_api_repository import SoccerApiRepository

class GetUpcomingMatches:
    def __init__(self, soccer_repository: SoccerApiRepository):
        self.soccer_repository = soccer_repository

    def __call__(self):
        try:
            return self.soccer_repository.get_upcoming_matches()
        except Exception as e:
            raise e
