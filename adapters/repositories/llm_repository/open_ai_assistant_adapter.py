import openai
from openai import AsyncOpenAI, OpenAI
from core.src.repositories import AIAssistantRepository


class OpenAIAssistantAdapter(AIAssistantRepository):

    def __init__(self, client: OpenAI):
        self.client = client
    
    def get_assistant(self, assistant_name: str):
        assistant = next(
            (x for x in self.client.beta.assistants.list() if x.name == assistant_name)
        )
        return assistant

    def create_thread(self):
        try:
            thread = self.client.beta.threads.create()
            return thread

        except openai.APIError as e:
            raise e

    def add_message(self, thread_id: str, role: str, message: str):
        try:
            message = self.client.beta.threads.messages.create(
                thread_id=thread_id, 
                role=role, 
                content=message
            )

            return message

        except openai.APIError as e:
            raise e

    def create_and_poll(self, thread_id: str, assistant_id: str):
        try:
            run = self.client.beta.threads.runs.create_and_poll(
                thread_id=thread_id,
                assistant_id=assistant_id,
                instructions="Please address the user as Jane Doe. The user has a premium account.",
            )

            return run

        except openai.APIError as e:
            raise e

    def list_messages(self, thread_id: str):
        try:
            format_messages = []

            messages = self.client.beta.threads.messages.list(thread_id=thread_id, order="asc")
            for message in messages.data:
                format_messages.append({
                    "role": message.role,
                    "message": message.content[0].text.value
                })

            return format_messages

        except openai.APIError as e:
            raise e
