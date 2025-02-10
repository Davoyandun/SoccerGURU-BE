from abc import ABC, abstractmethod


class SoccerApiRepository(ABC):
    @abstractmethod
    def get_upcoming_matches(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_statistics(self, team_id_1: str, team_id_2: str):
        raise NotImplementedError
