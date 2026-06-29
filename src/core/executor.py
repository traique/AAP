"""
AAP Core Executor

Thực thi ExecutionPlan.
"""

from __future__ import annotations

from typing import Any

from core.context import RequestContext
from core.models import ExecutionPlan, ToolResult
from core.tool import tool_registry


class Executor:
    """
    Thực thi từng Task trong ExecutionPlan.
    """

    async def execute(
        self,
        context: RequestContext,
        plan: ExecutionPlan,
    ) -> list[ToolResult]:

        results: list[ToolResult] = []

        for task in plan.tasks:

            tool = tool_registry.get(task.tool)

            result = await tool.execute(
                context=context,
                **task.input,
            )

            results.append(result)

        return results


executor = Executor()
