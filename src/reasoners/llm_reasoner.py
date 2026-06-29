"""
AAP LLM Reasoner

Convert a natural language request into a structured Goal.
"""

from __future__ import annotations

from adapters.llm.base import LLMAdapter
from core.context import RequestContext
from core.goal import Goal
from core.reasoning_engine import ReasoningEngine
from utils.json_parser import parse_json_object


SYSTEM_PROMPT = """
You are the reasoning engine of AAP.

Your job is NOT to answer the user.

Your ONLY job is to analyze the user's request and return ONE JSON object.

Return ONLY valid JSON.

Schema:

{
  "type": "...",
  "objective": "...",
  "confidence": 0.95,
  "entities": [],
  "constraints": [],
  "metadata": {}
}

Goal Types:

- chat
- image
- content
- multi_step
- vision
- document
- unknown
""".strip()


class LLMReasoner(ReasoningEngine):
    """
    Generic LLM-based Reasoning Engine.
    """

    def __init__(
        self,
        llm: LLMAdapter,
    ) -> None:

        self._llm = llm

    async def reason(
        self,
        context: RequestContext,
        message: str,
    ) -> Goal:
        """
        Convert user message into Goal.
        """

        response = await self._llm.generate(
            context=context,
            system_prompt=SYSTEM_PROMPT,
            prompt=message,
            temperature=0.0,
        )

        data = parse_json_object(
            response.text,
        )

        return Goal.model_validate(data)
