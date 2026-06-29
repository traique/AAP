"""
AAP Execution Plan
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from core.task import Task


class ExecutionPlan(BaseModel):
    """
    Danh sách Task sẽ được Runtime thực thi.
    """

    tasks: list[Task] = Field(
        default_factory=list,
    )

    def add(
        self,
        task: Task,
    ) -> None:

        self.tasks.append(task)

    def get(
        self,
        task_id: str,
    ) -> Task | None:

        for task in self.tasks:

            if task.id == task_id:
                return task

        return None
