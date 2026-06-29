"""
AAP Gemini Adapter

Bridge between AAP Runtime and GeminiClient.
"""

from __future__ import annotations

from typing import Any

from adapters.clients.gemini_client import (
    GeminiClient,
    GeminiResult,
)
from adapters.llm.base import (
    LLMAdapter,
    LLMResponse,
)
from core.context import RequestContext


class GeminiAdapter(LLMAdapter):
    """
    Gemini implementation of LLMAdapter.

    Responsibilities
    ----------------
    - Build final prompt
    - Call GeminiClient
    - Convert GeminiResult -> LLMResponse

    This class MUST NOT
    -------------------
    - Parse JSON
    - Know Goal
    - Know Planner
    - Know Telegram
    """

    name = "gemini"

    version = "2.0"

    supports_json = True

    supports_streaming = False

    supports_vision = True

    supports_tools = False

    supports_system_prompt = True

    def __init__(
        self,
        client: GeminiClient,
    ) -> None:
        self._client = client

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
        Generate text using Gemini.
        """

        final_prompt = self._merge_prompt(
            system_prompt=system_prompt,
            prompt=prompt,
        )

        result: GeminiResult = await self._client.generate(
            prompt=final_prompt,
            temperature=temperature,
            **kwargs,
        )

        return self._to_response(result)

    @staticmethod
    def _merge_prompt(
        *,
        system_prompt: str | None,
        prompt: str,
    ) -> str:
        """
        Merge system prompt and user prompt.
        """

        if not system_prompt:
            return prompt.strip()

        return (
            f"{system_prompt.strip()}\n\n"
            f"{prompt.strip()}"
        )

    @staticmethod
    def _to_response(
        result: GeminiResult,
    ) -> LLMResponse:
        """
        Convert GeminiResult into LLMResponse.
        """

        return LLMResponse(
            text=result.text,
            provider=result.provider,
            model=result.model,
            finish_reason=result.finish_reason,
            latency=result.latency,
            usage=result.usage,
            metadata={
                "images": len(result.images),
                "videos": len(result.videos),
            },
        )
