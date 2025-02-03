import os

from dotenv import load_dotenv
from openai import OpenAI

from adapters.repositories.llm_repository.open_ai_assistant_adapter import (
    OpenAIAssistantAdapter,
)


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def llm_repository():
    return OpenAIAssistantAdapter(client=client)
