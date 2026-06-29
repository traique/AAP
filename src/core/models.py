"""
AAP Runtime Models
"""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


# ==========================================================
# Status
# ==========================================================

class ToolStatus(str, Enum):

    SUCCESS = "success"

    FAILED = "failed"

    SKIPPED = "skipped"


# ==========================================================
# Tool Result
# ==========================================================

class ToolResult(BaseModel):
    """
    Standard result returned by every Tool.
    """

    status: ToolStatus

    tool: str

    provider: str | None = None

    text: str = ""

    metadata: dict[str, Any] = Field(
        default_factory=dict,
    )


# ==========================================================
# Image Result
# ==========================================================

class ImageResult(BaseModel):

    images: list[Any] = Field(
        default_factory=list,
    )


# ==========================================================
# Content Result
# ==========================================================

class ContentResult(BaseModel):

    content: str


# ==========================================================
# Chat Result
# ==========================================================

class ChatResult(BaseModel):

    message: str


# ==========================================================
# Execution Result
# ==========================================================

class ExecutionResult(BaseModel):

    success: bool = True

    results: list[ToolResult] = Field(
        default_factory=list,
    )
