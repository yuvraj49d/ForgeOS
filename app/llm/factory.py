from app.llm.providers.mock import MockProvider


def get_llm_provider():
    return MockProvider()