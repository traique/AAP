"""
AAP Core Provider Resolver

Chịu trách nhiệm chọn Provider phù hợp.
"""

from __future__ import annotations

from core.capabilities import Capability
from core.provider_manager import (
    ProviderInfo,
    provider_manager,
)
from core.policy import policy_engine


class ProviderResolver:
    """
    Resolve provider theo Capability và Policy.
    """

    def resolve(
        self,
        capability: Capability,
    ) -> ProviderInfo:

        providers = provider_manager.find(capability)

        if not providers:

            raise RuntimeError(
                f"No provider supports '{capability.value}'."
            )

        #
        # Hiện tại ProviderManager đã sort theo Policy.
        # Sau này có thể bổ sung:
        #
        # - Cost
        # - Health Score
        # - Region
        # - User Tier
        #

        return providers[0]


provider_resolver = ProviderResolver()
