from abc import ABC, abstractmethod
from typing import Any, Dict, List

class LLMClient(ABC):
    @abstractmethod
    def create_chat_completion(self, messages: List[Dict], tools: List[Dict]) -> Any:
        pass