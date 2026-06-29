"""
AAP Runtime

Main execution pipeline.
"""

from __future__ import annotations

from core.context import RequestContext
from core.executor import executor
from core.models import ExecutionPlan, ToolResult


class Runtime:

    def __init__(

        self,

        reasoner,

        planner,

    ):

        self.reasoner = reasoner

        self.planner = planner

    async def run(

        self,

        context: RequestContext,

        message: str,

    ) -> list[ToolResult]:

        #
        # 1
        # Reasoning
        #

        decision = await self.reasoner.reason(

            context=context,

            message=message,

        )

        #
        # 2
        # Planning
        #

        plan: ExecutionPlan = await self.planner.plan(

            context=context,

            goal=decision,

        )

        #
        # 3
        # Execute
        #

        results = await executor.execute(

            context=context,

            plan=plan,

        )

        return results
