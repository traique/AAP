"""
AAP Planner

Goal -> ExecutionPlan
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from core.context import RequestContext
from core.goal import Goal
from core.models import ExecutionPlan


class Planner(ABC):
    """
    Base Planner.
    """

    @abstractmethod
    async def create_plan(
        self,
        context: RequestContext,
        goal: Goal,
    ) -> ExecutionPlan:
        """
        Convert Goal into ExecutionPlan.
        """
        raise NotImplementedError
