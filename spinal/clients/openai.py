from openai import OpenAI
from typing import Any, Dict, List
from .base import LLMClient

class OpenAIClient(LLMClient):
    def __init__(self, model: str = "gpt-4o-mini"):
        self._client = OpenAI()
        self._model = model

    def create_chat_completion(self, messages: List[Dict], tools: List[Dict]) -> Any:
        return self._client.chat.completions.create(
            model=self._model,
            messages=messages,
            tools=tools
        )