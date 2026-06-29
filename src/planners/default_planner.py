"""
Default Planner
"""

from __future__ import annotations

from uuid import uuid4

from core.context import RequestContext
from core.goal import Goal, GoalType
from core.models import ExecutionPlan, Task
from core.planner import Planner


class DefaultPlanner(Planner):

    async def create_plan(
        self,
        context: RequestContext,
        goal: Goal,
    ) -> ExecutionPlan:

        tasks: list[Task] = []

        match goal.type:

            case GoalType.CHAT:

                tasks.append(
                    Task(
                        id=str(uuid4()),
                        tool="chat",
                        input={
                            "goal": goal.model_dump(),
                        },
                    )
                )

            case GoalType.CONTENT:

                tasks.append(
                    Task(
                        id=str(uuid4()),
                        tool="write_content",
                        input={
                            "goal": goal.model_dump(),
                        },
                    )
                )

            case GoalType.IMAGE:

                tasks.append(
                    Task(
                        id=str(uuid4()),
                        tool="generate_image",
                        input={
                            "goal": goal.model_dump(),
                        },
                    )
                )

            case GoalType.MULTI_STEP:

                #
                # Sprint sau
                #

                raise NotImplementedError(
                    "Multi-step planner chưa được triển khai."
                )

            case _:

                tasks.append(
                    Task(
                        id=str(uuid4()),
                        tool="chat",
                        input={
                            "goal": goal.model_dump(),
                        },
                    )
                )

        return ExecutionPlan(tasks=tasks)
