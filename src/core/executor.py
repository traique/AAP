"""
AAP Executor

Execute an ExecutionPlan.
"""

from __future__ import annotations

from core.context import RequestContext
from core.errors import ProviderNotFoundError
from core.models import ExecutionResult
from core.plan import ExecutionPlan
from core.provider_resolver import provider_resolver
from core.tool import tool_registry


class Executor:
    """
    Execute every task in an ExecutionPlan.
    """

    async def execute(
        self,
        context: RequestContext,
        plan: ExecutionPlan,
    ) -> ExecutionResult:

        execution = ExecutionResult()

        for task in plan.tasks:

            tool = tool_registry.get(task.tool)

            providers = provider_resolver.resolve_all(
                tool.manifest.capability,
            )

            if not providers:
                raise ProviderNotFoundError(
                    f"No provider found for capability "
                    f"'{tool.manifest.capability.value}'."
                )

            last_error: Exception | None = None

            for provider in providers:

                try:

                    result = await tool.execute(
                        context=context,
                        provider=provider.adapter,
                        **task.input,
                    )

                    execution.results.append(result)

                    last_error = None

                    #
                    # TODO
                    #
                    # metrics.record_success(...)
                    # health.record_success(...)
                    #

                    break

                except Exception as exc:

                    last_error = exc

                    #
                    # TODO
                    #
                    # metrics.record_failure(...)
                    # health.record_failure(...)
                    #

                    continue

            if last_error:

                execution.success = False

                raise last_error

        return execution
