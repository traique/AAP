"""
AAP Bootstrap

Application composition root.

This is the ONLY place where concrete implementations
are instantiated and wired together.
"""

from __future__ import annotations

import os

from adapters.clients.gemini_client import GeminiClient
from adapters.llm.base import LLMAdapter
from adapters.llm.gemini import GeminiAdapter

from core.container import container
from core.executor import Executor
from core.planner import Planner
from core.runtime import Runtime

from planners.default_planner import DefaultPlanner
from reasoners.llm_reasoner import LLMReasoner

from tools.chat import ChatTool
from core.tool import tool_registry


async def bootstrap() -> Runtime:
    """
    Build the application.
    """

    #
    # Gemini Client
    #

    gemini_client = GeminiClient(
        psid=os.environ["GEMINI_SECURE_1PSID"],
        psidts=os.getenv(
            "GEMINI_SECURE_1PSIDTS",
        ),
    )

    await gemini_client.initialize()

    #
    # Adapter
    #

    llm_adapter = GeminiAdapter(
        gemini_client,
    )

    container.register(
        LLMAdapter,
        llm_adapter,
    )

    #
    # Reasoner
    #

    reasoner = LLMReasoner(
        llm=container.resolve(
            LLMAdapter,
        )
    )

    #
    # Planner
    #

    planner: Planner = DefaultPlanner()

    #
    # Executor
    #

    executor = Executor()

    #
    # Tools
    #

    tool_registry.register(
        ChatTool(
            llm=container.resolve(
                LLMAdapter,
            )
        )
    )

    #
    # Runtime
    #

    runtime = Runtime(
        reasoner=reasoner,
        planner=planner,
        executor=executor,
    )

    return runtime
