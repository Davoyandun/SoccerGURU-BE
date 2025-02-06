from core.src.repositories import SoccerApiRepository, LLMRepository


class GetLLMPrediction:
    def __init__(
            self, 
            soccer_repository: SoccerApiRepository,
            llm_repository: LLMRepository
        ):
        self.soccer_repository = soccer_repository
        self.llm_repository = llm_repository
    def __call__(self, team_id_1: int, team_id_2: int):
        try:
            team_statistics = self.soccer_repository.get_statistics(team_id_1=team_id_1, team_id_2=team_id_2)

            # This is just as an example, the actual implementation will be different and it's up to you how to pass the data to the get_prediction method.
            # We need also to see how is the data coming from the get_statistics method
            #llm_prediction = self.llm_repository.get_prediction(data_team_1=team_statistics[0], data_team_2=team_statistics[1])
            return team_statistics
        except Exception as e:
            raise e
