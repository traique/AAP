"""
AAP Tool Manifest
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field

from core.capabilities import Capability


class ToolCategory(str, Enum):
    """
    Tool category.

    Used only for UI and organization.
    """

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

    #
    # Identity
    #

    name: str

    display_name: str

    description: str

    #
    # Runtime
    #

    capability: Capability

    category: ToolCategory

    #
    # Metadata
    #

    version: str = "1.0.0"

    author: str = "AAP"

    enabled: bool = True

    priority: int = 100

    timeout: int = 60

    #
    # Tags
    #

    tags: list[str] = Field(
        default_factory=list,
    )

    #
    # Schemas
    #

    input_schema: str | None = None

    output_schema: str | None = None
