"""
AI Assistant Platform (AAP)

core/tool.py

Tool Registry & Base Tool
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from core.context import RequestContext
from core.models import ToolResult


# ==========================================================
# Base Tool
# ==========================================================


class BaseTool(ABC):
    """
    Base class của mọi Tool.
    """

    name: str = ""

    description: str = ""

    version: str = "1.0.0"

    enabled: bool = True

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


# ==========================================================
# Registry
# ==========================================================


class ToolRegistry:

    def __init__(self):

        self._tools: dict[str, BaseTool] = {}

    def register(
        self,
        tool: BaseTool,
    ) -> None:

        if tool.name in self._tools:

            raise ValueError(
                f"Tool '{tool.name}' already registered."
            )

        self._tools[tool.name] = tool

    def unregister(
        self,
        name: str,
    ) -> None:

        self._tools.pop(name, None)

    def get(
        self,
        name: str,
    ) -> BaseTool:

        if name not in self._tools:

            raise KeyError(
                f"Tool '{name}' not found."
            )

        return self._tools[name]

    def exists(
        self,
        name: str,
    ) -> bool:

        return name in self._tools

    def list(self) -> list[str]:

        return sorted(self._tools.keys())

    async def execute(
        self,
        name: str,
        context: RequestContext,
        **kwargs: Any,
    ) -> ToolResult:

        tool = self.get(name)

        return await tool.execute(
            context=context,
            **kwargs,
        )


tool_registry = ToolRegistry()


# ==========================================================
# Decorator
# ==========================================================


def tool(
    *,
    name: str,
    description: str,
):
    """
    Register tool automatically.
    """

    def wrapper(cls):

        instance = cls()

        instance.name = name

        instance.description = description

        tool_registry.register(instance)

        return cls

    return wrapper
