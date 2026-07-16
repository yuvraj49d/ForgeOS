from pydantic import BaseModel


class LLMResponse(BaseModel):
    text: str

    model: str

    provider: str

    prompt_tokens: int | None = None

    completion_tokens: int | None = None