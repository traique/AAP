"""
AAP Runtime

Main execution pipeline.
"""

from __future__ import annotations

from core.context import RequestContext
from core.executor import Executor
from core.models import ExecutionResult
from core.plan import ExecutionPlan
from core.planner import Planner
from core.reasoning_engine import ReasoningEngine


class Runtime:
    """
    Main runtime of AAP.
    """

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
    ) -> ExecutionResult:
        """
        Execute a complete request.
        """

        #
        # Step 1
        # Reasoning
        #

        goal = await self._reasoner.reason(
            context=context,
            message=message,
        )

        #
        # Step 2
        # Planning
        #

        plan: ExecutionPlan = await self._planner.create_plan(
            context=context,
            goal=goal,
        )

        #
        # Step 3
        # Execute
        #

        return await self._executor.execute(
            context=context,
            plan=plan,
        )
