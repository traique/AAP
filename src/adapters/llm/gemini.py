"""
AAP Gemini Adapter

LLM Adapter implementation for Gemini.
"""

from __future__ import annotations

import json

from adapters.llm.base import (
    LLMAdapter,
    LLMResponse,
)
from core.context import RequestContext


class GeminiAdapter(LLMAdapter):
    """
    Gemini Adapter.

    Không phụ thuộc trực tiếp vào gemini-webapi.
    Chỉ làm việc với GeminiClient.
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
        client,
    ):

        self.client = client

    async def generate(
        self,
        *,
        context: RequestContext,
        prompt: str,
        system_prompt: str | None = None,
        temperature: float = 0.7,
        **kwargs,
    ) -> LLMResponse:

        #
        # Ghép System Prompt
        #

        final_prompt = prompt

        if system_prompt:

            final_prompt = (
                f"{system_prompt}\n\n"
                f"{prompt}"
            )

        #
        # Call Gemini Client
        #

        result = await self.client.generate(
            prompt=final_prompt,
            temperature=temperature,
            **kwargs,
        )

        return LLMResponse(
            text=result.text,
            usage=getattr(result, "usage", {}),
            finish_reason=getattr(
                result,
                "finish_reason",
                None,
            ),
        )

    async def generate_json(
        self,
        *,
        context: RequestContext,
        prompt: str,
        system_prompt: str | None = None,
        **kwargs,
    ) -> dict:

        response = await self.generate(
            context=context,
            prompt=prompt,
            system_prompt=system_prompt,
            **kwargs,
        )

        #
        # Validate JSON
        #

        return json.loads(response.text)
