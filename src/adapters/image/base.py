"""
AAP Image Adapter

Base interface for image generation providers.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from core.context import RequestContext

from .response import ImageResponse


class ImageAdapter(ABC):
    """
    Base interface for all image providers.
    """

    name: str = "unknown"

    version: str = "1.0"

    supports_negative_prompt: bool = True

    supports_seed: bool = False

    supports_upscale: bool = False

    supports_img2img: bool = False

    supports_controlnet: bool = False

    @abstractmethod
    async def generate(
        self,
        *,
        context: RequestContext,
        prompt: str,
        negative_prompt: str = "",
        aspect_ratio: str = "1:1",
        seed: int | None = None,
        **kwargs: Any,
    ) -> ImageResponse:
        """
        Generate image.
        """
        raise NotImplementedError
