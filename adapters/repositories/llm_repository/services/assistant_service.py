import openai
from openai import AsyncOpenAI


class OpenAIAssistantAPI:

    def __init__(self, client: AsyncOpenAI):
        self.client = client

    async def create_thread(self):
        try:
            thread = await self.client.beta.threads.create()
            return thread

        except openai.APIError as e:
            raise e

    async def add_message(self, thread_id: str, role: str, message: str):
        try:
            message = await self.client.beta.threads.messages.create(
                thread_id=thread_id, 
                role=role, 
                content=message
            )

            return message

        except openai.APIError as e:
            raise e

    async def create_and_poll(self, thread_id: str, assistant_id: str):
        try:
            run = await self.client.beta.threads.runs.create_and_poll(
                thread_id=thread_id,
                assistant_id=assistant_id,
                instructions="Please address the user as Jane Doe. The user has a premium account.",
            )

            return run

        except openai.APIError as e:
            raise e

    async def list_messages(self, thread_id: str):
        try:
            messages = await self.client.beta.threads.messages.list(thread_id=thread_id)
            return messages

        except openai.APIError as e:
            raise e
