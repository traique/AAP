"""
AAP Image Response
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class ImageResponse(BaseModel):
    """
    Standard response returned by every image provider.
    """

    provider: str

    model: str

    images: list[str] = Field(default_factory=list)

    latency: float | None = None

    metadata: dict[str, Any] = Field(default_factory=dict)
