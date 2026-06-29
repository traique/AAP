"""
AAP Executor

Execute an ExecutionPlan.
"""

from __future__ import annotations

from core.capabilities import Capability
from core.context import RequestContext
from core.models import ToolResult
from core.plan import ExecutionPlan
from core.provider_resolver import provider_resolver
from core.tool import tool_registry


class Executor:
    """
    Execute every task inside an ExecutionPlan.
    """

    async def execute(
        self,
        context: RequestContext,
        plan: ExecutionPlan,
    ) -> list[ToolResult]:

        results: list[ToolResult] = []

        for task in plan.tasks:

            tool = tool_registry.get(task.tool)

            capability: Capability = tool.manifest.category.to_capability()

            providers = provider_resolver.resolve_all(
                capability,
            )

            last_error: Exception | None = None

            for provider in providers:

                try:

                    result = await tool.execute(
                        context=context,
                        provider=provider.adapter,
                        **task.input,
                    )

                    results.append(result)

                    last_error = None

                    break

                except Exception as exc:

                    last_error = exc

                    #
                    # TODO
                    # metrics
                    # circuit breaker
                    #

                    continue

            if last_error:

                raise last_error

        return results
