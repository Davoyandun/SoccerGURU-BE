from openai import OpenAI

from config import OPENAI_API_KEY
from adapters.repositories.llm_repository.open_ai_assistant_adapter import (
    OpenAIAssistantAdapter,
)


client = OpenAI(api_key=OPENAI_API_KEY)


def llm_repository():
    return OpenAIAssistantAdapter(client=client)
