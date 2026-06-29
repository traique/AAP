"""
Gemini Reasoner
"""

from __future__ import annotations

import json

from core.context import RequestContext
from core.goal import Goal
from core.reasoning_engine import ReasoningEngine
from providers.gemini import GeminiProvider


class GeminiReasoner(ReasoningEngine):

    def __init__(
        self,
        provider: GeminiProvider,
    ):

        self.provider = provider

    async def reason(
        self,
        context: RequestContext,
        message: str,
    ) -> Goal:

        prompt = self._build_prompt(message)

        response = await self.provider.chat(
            prompt=prompt,
        )

        #
        # Validate JSON
        #

        data = json.loads(response)

        return Goal.model_validate(data)

    def _build_prompt(
        self,
        message: str,
    ) -> str:

        return f"""
You are the AAP Reasoning Engine.

Return ONLY valid JSON.

Output schema:

{{
    "type": "...",
    "objective": "...",
    "confidence": 0.95,
    "entities": [],
    "constraints": []
}}

User:

{message}
"""
