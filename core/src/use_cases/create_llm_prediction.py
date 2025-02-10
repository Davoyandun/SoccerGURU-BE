from core.src.repositories import AIAssistantRepository, SoccerApiRepository
from config import PREDICTION_PROMPT
class CreatePrediction:
    def __init__(
            self, 
            ai_assistant_repository: AIAssistantRepository,
            soccer_repository: SoccerApiRepository,
        ):
        self.ai_assistant_repository = ai_assistant_repository
        self.soccer_repository = soccer_repository


    def __call__(self, assistant_name: str, home_team_id: str, away_team_id: str):
        try:
            assistant = self.ai_assistant_repository.get_assistant(assistant_name=assistant_name)
            team_statistics = self.soccer_repository.get_statistics(team_id_1=home_team_id, team_id_2=away_team_id)

            thread_id = self.ai_assistant_repository.create_thread()
            if not thread_id.id:
                raise Exception("Thread id was not create success")

            self.ai_assistant_repository.add_message(
                thread_id=thread_id.id, 
                role="user", 
                message=f"{PREDICTION_PROMPT} {team_statistics}"
            )

            run = self.ai_assistant_repository.create_and_poll(
                thread_id=thread_id.id, 
                assistant_id=assistant.id
            )
            if run.status != "completed":
                raise Exception(f"The status is: {run.status}")
            
            messages = self.ai_assistant_repository.list_messages(thread_id=thread_id.id)

            return messages
        except Exception as e:
            raise e
