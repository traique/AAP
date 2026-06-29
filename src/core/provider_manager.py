"""
AAP Provider Manager
"""

from __future__ import annotations

from dataclasses import dataclass, field

from core.capabilities import Capability


@dataclass(slots=True)
class ProviderDescriptor:
    """
    Provider metadata.
    """

    name: str

    adapter: object

    capabilities: set[Capability]

    priority: int = 100

    score: int = 100

    enabled: bool = True

    metadata: dict = field(default_factory=dict)


class ProviderManager:

    def __init__(self) -> None:

        self._providers: list[
            ProviderDescriptor
        ] = []

    def register(
        self,
        provider: ProviderDescriptor,
    ) -> None:

        self._providers.append(provider)

    def all(self) -> list[
        ProviderDescriptor
    ]:

        return list(self._providers)


provider_manager = ProviderManager()
