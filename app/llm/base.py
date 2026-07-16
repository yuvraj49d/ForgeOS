from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):
    """
    Base interface for every LLM provider.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate a response from the language model.
        """
        raise NotImplementedError