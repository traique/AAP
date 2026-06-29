"""
AAP AI Horde Adapter
"""

from __future__ import annotations

from adapters.image.base import ImageAdapter
from adapters.image.response import ImageResponse
from core.context import RequestContext


class AIHordeAdapter(ImageAdapter):
    """
    AI Horde implementation.
    """

    name = "ai_horde"

    version = "1.0"

    supports_seed = True

    supports_negative_prompt = True

    async def generate(
        self,
        *,
        context: RequestContext,
        prompt: str,
        negative_prompt: str = "",
        aspect_ratio: str = "1:1",
        seed: int | None = None,
        **kwargs,
    ) -> ImageResponse:
        """
        Generate image using AI Horde.

        TODO:
        - submit generation
        - poll status
        - download images
        """

        raise NotImplementedError(
            "AI Horde adapter not implemented yet."
        )
