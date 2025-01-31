from abc import ABC, abstractmethod


class LLMRepository(ABC):
    @abstractmethod
    def get_prediction(self, data_team_1: dict, data_team_2: int):
        raise NotImplementedError
