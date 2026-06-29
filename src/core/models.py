"""
AI Assistant Platform (AAP)

core/models.py

Shared runtime models.
"""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


# ==========================================================
# ENUMS
# ==========================================================


class ToolStatus(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"
    SKIPPED = "skipped"


class ActionType(str, Enum):
    CHAT = "chat"

    IMAGE = "image"

    CONTENT = "content"

    VISION = "vision"

    DOCUMENT = "document"

    MEMORY = "memory"

    UNKNOWN = "unknown"


# ==========================================================
# DECISION
# ==========================================================


class Decision(BaseModel):
    """
    Output của Decision Engine.
    """

    action: ActionType

    confidence: float = Field(
        ge=0.0,
        le=1.0,
    )

    reason: str | None = None

    metadata: dict[str, Any] = Field(
        default_factory=dict,
    )


# ==========================================================
# TASK
# ==========================================================


class Task(BaseModel):
    """
    Một bước trong Execution Plan.
    """

    id: str

    tool: str

    input: dict[str, Any] = Field(
        default_factory=dict,
    )


# ==========================================================
# PLAN
# ==========================================================


class ExecutionPlan(BaseModel):
    """
    Danh sách Task.
    """

    tasks: list[Task] = Field(
        default_factory=list,
    )


# ==========================================================
# RESULT
# ==========================================================


class ToolResult(BaseModel):
    """
    Kết quả trả về của Tool.
    """

    status: ToolStatus

    tool: str

    provider: str | None = None

    text: str | None = None

    images: list[str] = Field(
        default_factory=list,
    )

    files: list[str] = Field(
        default_factory=list,
    )

    metadata: dict[str, Any] = Field(
        default_factory=dict,
    )

    error: str | None = None
