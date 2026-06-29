"""
AAP Runtime
"""

from __future__ import annotations

from core.context import RequestContext
from core.executor import Executor
from core.plan import ExecutionPlan
from core.planner import Planner
from core.reasoning_engine import ReasoningEngine


class Runtime:

    def __init__(
        self,
        *,
        reasoner: ReasoningEngine,
        planner: Planner,
        executor: Executor,
    ) -> None:

        self._reasoner = reasoner
        self._planner = planner
        self._executor = executor

    async def run(
        self,
        context: RequestContext,
        message: str,
    ):

        goal = await self._reasoner.reason(
            context=context,
            message=message,
        )

        plan: ExecutionPlan = await self._planner.create_plan(
            context=context,
            goal=goal,
        )

        return await self._executor.execute(
            context=context,
            plan=plan,
        )
