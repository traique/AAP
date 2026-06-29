"""
AAP Bootstrap
"""

from __future__ import annotations

import os

from adapters.clients.gemini_client import GeminiClient
from adapters.llm.base import LLMAdapter
from adapters.llm.gemini import GeminiAdapter

from core.container import container
from core.executor import Executor
from core.provider_manager import (
    ProviderDescriptor,
    provider_manager,
)
from core.runtime import Runtime

from planners.default_planner import DefaultPlanner
from reasoners.llm_reasoner import LLMReasoner

from tools.chat import ChatTool
from core.tool import tool_registry

from core.capabilities import Capability


async def bootstrap() -> Runtime:

    #
    # Client
    #

    client = GeminiClient(
        psid=os.environ["GEMINI_SECURE_1PSID"],
        psidts=os.getenv(
            "GEMINI_SECURE_1PSIDTS",
        ),
    )

    await client.initialize()

    #
    # Adapter
    #

    llm = GeminiAdapter(
        client,
    )

    container.register(
        LLMAdapter,
        llm,
    )

    #
    # Provider
    #

    provider_manager.register(
        ProviderDescriptor(
            name="gemini",
            adapter=llm,
            capabilities={
                Capability.CHAT,
                Capability.CONTENT_WRITING,
                Capability.VISION,
            },
            priority=10,
            score=60,
        )
    )

    #
    # Tool
    #

    tool_registry.register(
        ChatTool(
            llm=container.resolve(
                LLMAdapter,
            ),
        )
    )

    #
    # Runtime
    #

    runtime = Runtime(
        reasoner=LLMReasoner(llm),
        planner=DefaultPlanner(),
        executor=Executor(),
    )

    return runtime
