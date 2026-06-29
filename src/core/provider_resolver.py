"""
AAP Provider Resolver
"""

from __future__ import annotations

from core.capabilities import Capability
from core.provider_manager import (
    ProviderDescriptor,
    provider_manager,
)


class ProviderResolver:
    """
    Resolve providers for a capability.
    """

    def resolve_all(
        self,
        capability: Capability,
    ) -> list[
        ProviderDescriptor
    ]:

        providers = [

            provider

            for provider in provider_manager.all()

            if (
                provider.enabled
                and capability
                in provider.capabilities
            )
        ]

        providers.sort(

            key=lambda p: (
                p.score,
                -p.priority,
            ),

            reverse=True,
        )

        return providers


provider_resolver = ProviderResolver()
