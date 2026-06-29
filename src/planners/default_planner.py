"""
AAP Default Planner
"""

from __future__ import annotations

from uuid import uuid4

from core.context import RequestContext
from core.goal import Goal, GoalType
from core.plan import ExecutionPlan
from core.planner import Planner
from core.task import Task


class DefaultPlanner(Planner):
    """
    Default planner implementation.
    """

    async def create_plan(
        self,
        context: RequestContext,
        goal: Goal,
    ) -> ExecutionPlan:

        plan = ExecutionPlan()

        match goal.type:

            case GoalType.CHAT:

                plan.add(
                    Task(
                        id=str(uuid4()),
                        name="General Chat",
                        tool="chat",
                        input={
                            "message": goal.objective,
                        },
                    )
                )

            case GoalType.CONTENT:

                plan.add(
                    Task(
                        id=str(uuid4()),
                        name="Write Content",
                        tool="content",
                        input={
                            "goal": goal,
                        },
                    )
                )

            case GoalType.IMAGE:

                plan.add(
                    Task(
                        id=str(uuid4()),
                        name="Generate Image",
                        tool="generate_image",
                        input={
                            "goal": goal,
                        },
                    )
                )

            case _:

                plan.add(
                    Task(
                        id=str(uuid4()),
                        name="Fallback Chat",
                        tool="chat",
                        input={
                            "message": goal.objective,
                        },
                    )
                )

        return plan
