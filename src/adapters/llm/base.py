"""
AAP LLM Base Adapter

Common models and interfaces for all LLM adapters.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel, Field

from core.context import RequestContext


class TokenUsage(BaseModel):
    """
    Token usage statistics.
    """

    prompt_tokens: int = 0

    completion_tokens: int = 0

    total_tokens: int = 0


class LLMResponse(BaseModel):
    """
    Standard response returned by every LLM adapter.
    """

    text: str = ""

    provider: str

    model: str

    finish_reason: str | None = None

    latency: float | None = None

    usage: TokenUsage = Field(
        default_factory=TokenUsage,
    )

    metadata: dict[str, Any] = Field(
        default_factory=dict,
    )


class LLMAdapter(ABC):
    """
    Base interface for all Large Language Models.
    """

    name: str = "unknown"

    version: str = "1.0"

    supports_json: bool = True

    supports_streaming: bool = False

    supports_vision: bool = False

    supports_tools: bool = False

    supports_system_prompt: bool = True

    @abstractmethod
    async def generate(
        self,
        *,
        context: RequestContext,
        prompt: str,
        system_prompt: str | None = None,
        temperature: float = 0.7,
        **kwargs: Any,
    ) -> LLMResponse:
        """
        Generate text.
        """
        raise NotImplementedError
