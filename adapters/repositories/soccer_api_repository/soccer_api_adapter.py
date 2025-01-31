from core.src.repositories import SoccerApiRepository

class UEFAChampionsLeagueApiAdapter(SoccerApiRepository):
    def get_upcoming_matches(self):
        raise NotImplementedError
    
    def get_statistics(self, team_id_1: int, team_id_2: int):
        raise NotImplementedError
