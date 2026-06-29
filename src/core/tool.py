"""
AAP Tool Framework
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from core.context import RequestContext
from core.manifest import ToolManifest
from core.models import ToolResult


class BaseTool(ABC):
    """
    Base class of every Tool.
    """

    manifest: ToolManifest

    @abstractmethod
    async def execute(
        self,
        context: RequestContext,
        **kwargs: Any,
    ) -> ToolResult:
        """
        Execute tool.
        """
        raise NotImplementedError


class ToolRegistry:
    """
    Runtime Tool Registry.

    Stores Tool instances.
    """

    def __init__(self) -> None:

        self._tools: dict[str, BaseTool] = {}

    def register(
        self,
        tool: BaseTool,
    ) -> None:

        name = tool.manifest.name

        if name in self._tools:

            raise ValueError(
                f"Tool '{name}' already registered."
            )

        self._tools[name] = tool

    def unregister(
        self,
        name: str,
    ) -> None:

        self._tools.pop(name, None)

    def get(
        self,
        name: str,
    ) -> BaseTool:

        try:

            return self._tools[name]

        except KeyError as exc:

            raise KeyError(
                f"Tool '{name}' not found."
            ) from exc

    def exists(
        self,
        name: str,
    ) -> bool:

        return name in self._tools

    def list(
        self,
    ) -> list[str]:

        return sorted(self._tools.keys())


tool_registry = ToolRegistry()
