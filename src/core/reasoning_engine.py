"""
AAP Reasoning Engine

Responsible for converting a user request into a structured Goal.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from core.context import RequestContext
from core.goal import Goal


class ReasoningEngine(ABC):
    """
    Base Reasoning Engine.
    """

    @abstractmethod
    async def reason(
        self,
        context: RequestContext,
        message: str,
    ) -> Goal:
        """
        Convert user message to Goal.
        """
        raise NotImplementedError
