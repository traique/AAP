"""
AAP LLM Adapter

Base interface for every LLM.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from core.context import RequestContext


class LLMResponse:

    def __init__(
        self,
        *,
        text: str = "",
        usage: dict[str, Any] | None = None,
        finish_reason: str | None = None,
    ):

        self.text = text

        self.usage = usage or {}

        self.finish_reason = finish_reason


class LLMAdapter(ABC):
    """
    Base class của mọi Large Language Model.
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

    async def generate_json(
        self,
        *,
        context: RequestContext,
        prompt: str,
        system_prompt: str | None = None,
        **kwargs: Any,
    ) -> dict:

        response = await self.generate(
            context=context,
            prompt=prompt,
            system_prompt=system_prompt,
            **kwargs,
        )

        import json

        return json.loads(response.text)
