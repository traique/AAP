"""
AAP Image Tool

Generate images using the best available provider.
"""

from __future__ import annotations

from adapters.image.base import ImageAdapter
from core.context import RequestContext
from core.manifest import ToolCategory, ToolManifest
from core.models import ToolResult, ToolStatus
from core.prompt_manager import prompt_manager
from core.provider_resolver import provider_resolver
from core.capabilities import Capability
from core.tool import BaseTool


class ImageTool(BaseTool):
    """
    AI image generation tool.
    """

    manifest = ToolManifest(
        name="generate_image",
        display_name="Generate Image",
        description="Generate AI images.",
        category=ToolCategory.IMAGE,
        tags=[
            "image",
            "ai",
            "art",
        ],
    )

    async def execute(
        self,
        context: RequestContext,
        **kwargs,
    ) -> ToolResult:

        prompt: str = kwargs["prompt"]

        aspect_ratio = kwargs.get(
            "aspect_ratio",
            "1:1",
        )

        negative_prompt = kwargs.get(
            "negative_prompt",
            "",
        )

        provider: ImageAdapter = provider_resolver.resolve(
            Capability.IMAGE_GENERATION,
        )

        response = await provider.generate(
            context=context,
            prompt=prompt,
            negative_prompt=negative_prompt,
            aspect_ratio=aspect_ratio,
        )

        return ToolResult(
            status=ToolStatus.SUCCESS,
            tool=self.manifest.name,
            provider=response.provider,
            text="Image generated successfully.",
            metadata={
                "images": response.images,
                "model": response.model,
                "latency": response.latency,
            },
  )
