"""
AAP Chat Tool
"""

from __future__ import annotations

from adapters.llm.base import LLMAdapter

from core.context import RequestContext
from core.manifest import (
    ToolCategory,
    ToolManifest,
)

from core.capabilities import Capability

from core.models import (
    ToolResult,
    ToolStatus,
)

from core.tool import BaseTool


class ChatTool(BaseTool):

    manifest = ToolManifest(
        name="chat",

        display_name="Chat",

        description="General conversation.",

        capability=Capability.CHAT,

        category=ToolCategory.CHAT,
    )

    def __init__(
        self,
    ) -> None:

        pass

    async def execute(
        self,
        context: RequestContext,
        *,
        provider: LLMAdapter,
        message: str,
        **kwargs,
    ) -> ToolResult:

        response = await provider.generate(
            context=context,
            prompt=message,
        )

        return ToolResult(
            status=ToolStatus.SUCCESS,

            tool=self.manifest.name,

            provider=response.provider,

            text=response.text,

            metadata={
                "model": response.model,
                "usage": response.usage.model_dump(),
            },
        )
