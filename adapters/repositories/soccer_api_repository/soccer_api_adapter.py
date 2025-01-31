from core.src.repositories import SoccerApiRepository

class UEFAChampionsLeagueApiAdapter(SoccerApiRepository):

    #This methods are gonna call the api (UEFA champions league, something like that, ask to DY) and return the data
    def get_upcoming_matches(self):
        raise NotImplementedError
    
    def get_statistics(self, team_id_1: int, team_id_2: int):
        raise NotImplementedError
