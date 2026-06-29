"""
AAP Task Model
"""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class TaskStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    SKIPPED = "skipped"


class Task(BaseModel):
    """
    Một bước thực thi.
    """

    id: str

    tool: str

    name: str

    input: dict[str, Any] = Field(
        default_factory=dict,
    )

    depends_on: list[str] = Field(
        default_factory=list,
    )

    retry: int = 2

    timeout: int = 60

    status: TaskStatus = TaskStatus.PENDING
