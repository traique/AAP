"""
AAP Core Contracts

Mọi thành phần trong hệ thống đều giao tiếp thông qua các Contract.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from core.context import RequestContext
from core.models import ToolResult


class Tool(ABC):
    """
    Base Tool.
    """

    @abstractmethod
    async def execute(
        self,
        context: RequestContext,
        **kwargs,
    ) -> ToolResult:
        ...


class Provider(ABC):
    """
    Base AI Provider.
    """

    @abstractmethod
    async def generate(
        self,
        **kwargs,
    ):
        ...


class Planner(ABC):
    """
    Planner Contract.
    """

    @abstractmethod
    async def plan(
        self,
        context: RequestContext,
        goal,
    ):
        ...


class ReasoningEngine(ABC):
    """
    AI Reasoning Engine.
    """

    @abstractmethod
    async def reason(
        self,
        context: RequestContext,
        message: str,
    ):
        ...
