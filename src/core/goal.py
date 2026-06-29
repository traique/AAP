"""
AAP Goal Model

Reasoning Engine -> Goal
Planner -> ExecutionPlan
"""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class GoalType(str, Enum):
    CHAT = "chat"

    IMAGE = "image"

    CONTENT = "content"

    MULTI_STEP = "multi_step"

    DOCUMENT = "document"

    VISION = "vision"

    UNKNOWN = "unknown"


class Entity(BaseModel):
    """
    Entity được AI trích xuất.
    """

    name: str

    value: str

    confidence: float = Field(
        default=1.0,
        ge=0,
        le=1,
    )


class Constraint(BaseModel):
    """
    Các ràng buộc.
    """

    key: str

    value: Any


class Goal(BaseModel):
    """
    Goal được sinh bởi Reasoning Engine.
    """

    type: GoalType

    objective: str

    confidence: float = Field(
        default=1.0,
        ge=0,
        le=1,
    )

    entities: list[Entity] = Field(
        default_factory=list,
    )

    constraints: list[Constraint] = Field(
        default_factory=list,
    )

    metadata: dict[str, Any] = Field(
        default_factory=dict,
  )
