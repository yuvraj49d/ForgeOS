from app.llm.base import BaseLLMProvider
from app.llm.models import LLMResponse


class MockProvider(BaseLLMProvider):

    def generate(self, prompt: str) -> LLMResponse:

        return LLMResponse(
            text="""
1. Analyze requirements
2. Design architecture
3. Implement solution
4. Write tests
5. Review implementation
""",
            model="mock-model",
            provider="mock",
        )