"""
AI Assistant Platform (AAP)

Tool Manifest
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class ToolCategory(str, Enum):
    CHAT = "chat"
    IMAGE = "image"
    CONTENT = "content"
    DOCUMENT = "document"
    VISION = "vision"
    MEMORY = "memory"
    SYSTEM = "system"


class ToolManifest(BaseModel):
    """
    Tool metadata.
    """

    name: str

    display_name: str

    description: str

    category: ToolCategory

    version: str = "1.0.0"

    author: str = "AAP"

    enabled: bool = True

    priority: int = 100

    tags: list[str] = Field(default_factory=list)

    input_schema: str | None = None

    output_schema: str | None = None

    timeout: int = 60
