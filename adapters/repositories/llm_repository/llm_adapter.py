from core.src.repositories import LLMRepository

class OpenAiAdapter(LLMRepository):
    def get_prediction(self, data_team_1, data_team_2):
        raise NotImplementedError
