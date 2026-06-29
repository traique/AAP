"""
AAP Core Policy Engine

Quyết định chiến lược lựa chọn Tool và Provider.
"""

from __future__ import annotations

from enum import Enum
from pydantic import BaseModel, Field

from core.capabilities import Capability


class SelectionStrategy(str, Enum):
    """
    Chiến lược lựa chọn Provider.
    """

    PRIORITY = "priority"

    BEST_SCORE = "best_score"

    LOWEST_COST = "lowest_cost"

    FASTEST = "fastest"

    ROUND_ROBIN = "round_robin"

    RANDOM = "random"


class CapabilityPolicy(BaseModel):
    """
    Policy cho một Capability.
    """

    capability: Capability

    strategy: SelectionStrategy = SelectionStrategy.BEST_SCORE

    allow_fallback: bool = True

    timeout: int = 60

    max_retry: int = 2


class PolicyEngine:
    """
    Runtime Policy Engine.
    """

    def __init__(self):

        self._policies: dict[Capability, CapabilityPolicy] = {}

    def register(
        self,
        policy: CapabilityPolicy,
    ) -> None:

        self._policies[policy.capability] = policy

    def get(
        self,
        capability: Capability,
    ) -> CapabilityPolicy:

        if capability in self._policies:
            return self._policies[capability]

        return CapabilityPolicy(
            capability=capability,
        )


policy_engine = PolicyEngine()
