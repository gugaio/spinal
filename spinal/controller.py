from typing import Dict, List, Optional
from .clients.base import LLMClient
from .clients.openai import OpenAIClient
from .serializers.message import MessageSerializer

class SpinalController:
    def __init__(self, llm_client: Optional[LLMClient] = None):
        self._llm = llm_client or OpenAIClient()

    def handle(self, messages: List[Dict], tools: List[Dict]) -> Dict[str, any]:
        response = self._llm.create_chat_completion(messages, tools)
        return self._serialize_llm_response(response)

    def _serialize_llm_response(self, response: any) -> Dict[str, any]:
        message = response.choices[0].message
        return MessageSerializer.serialize_message(message)