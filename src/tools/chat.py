"""
AAP Chat Tool

General conversation tool.
"""

from __future__ import annotations

from adapters.llm.base import LLMAdapter
from core.context import RequestContext
from core.manifest import ToolCategory, ToolManifest
from core.models import ToolResult, ToolStatus
from core.prompt_manager import prompt_manager
from core.tool import BaseTool, tool


@tool(
    manifest=ToolManifest(
        name="chat",
        display_name="Chat",
        description="General conversation using an LLM.",
        category=ToolCategory.CHAT,
        tags=[
            "chat",
            "conversation",
            "llm",
        ],
    )
)
class ChatTool(BaseTool):
    """
    General chat tool.
    """

    def __init__(
        self,
        llm: LLMAdapter,
    ) -> None:

        self._llm = llm

    async def execute(
        self,
        context: RequestContext,
        **kwargs,
    ) -> ToolResult:
        """
        Execute chat request.
        """

        message: str = kwargs["message"]

        history = kwargs.get(
            "history",
            "",
        )

        profile = kwargs.get(
            "profile",
            "",
        )

        prompt = prompt_manager.render(
            "chat",
            language=context.user.language,
            profile=profile,
            history=history,
            message=message,
        )

        response = await self._llm.generate(
            context=context,
            prompt=prompt,
        )

        return ToolResult(
            status=ToolStatus.SUCCESS,
            tool="chat",
            provider=response.provider,
            text=response.text,
            metadata={
                "model": response.model,
                "latency": response.latency,
                "usage": response.usage.model_dump(),
            },
        )
