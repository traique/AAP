"""
AI Assistant Platform (AAP)

core/provider_manager.py

Provider Runtime Manager
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta

from core.capabilities import Capability
from core.contracts import Provider
from core.policy import (
    SelectionStrategy,
    policy_engine,
)


@dataclass(slots=True)
class ProviderState:
    """
    Runtime state của Provider.
    """

    healthy: bool = True

    failure_count: int = 0

    success_count: int = 0

    last_error: str | None = None

    disabled_until: datetime | None = None


@dataclass(slots=True)
class ProviderInfo:
    """
    Metadata của Provider.
    """

    name: str

    provider: Provider

    capabilities: set[Capability]

    priority: int = 100

    score: int = 100

    enabled: bool = True

    state: ProviderState = field(
        default_factory=ProviderState,
    )


class ProviderManager:

    def __init__(self):

        self._providers: dict[str, ProviderInfo] = {}

    # ==========================================================
    # REGISTER
    # ==========================================================

    def register(
        self,
        provider: ProviderInfo,
    ):

        if provider.name in self._providers:

            raise ValueError(
                f"Provider '{provider.name}' already exists."
            )

        self._providers[provider.name] = provider

    # ==========================================================
    # FIND
    # ==========================================================

    def find(
        self,
        capability: Capability,
    ) -> list[ProviderInfo]:

        candidates = []

        now = datetime.now(UTC)

        for provider in self._providers.values():

            if not provider.enabled:
                continue

            if capability not in provider.capabilities:
                continue

            if (
                provider.state.disabled_until
                and provider.state.disabled_until > now
            ):
                continue

            candidates.append(provider)

        policy = policy_engine.get(capability)

        if policy.strategy == SelectionStrategy.PRIORITY:

            candidates.sort(
                key=lambda p: p.priority
            )

        elif policy.strategy == SelectionStrategy.BEST_SCORE:

            candidates.sort(
                key=lambda p: p.score,
                reverse=True,
            )

        return candidates

    # ==========================================================
    # SUCCESS
    # ==========================================================

    def report_success(
        self,
        name: str,
    ):

        provider = self._providers[name]

        provider.state.success_count += 1

        provider.state.failure_count = 0

        provider.state.last_error = None

        provider.state.disabled_until = None

    # ==========================================================
    # FAILURE
    # ==========================================================

    def report_failure(
        self,
        name: str,
        error: str,
    ):

        provider = self._providers[name]

        provider.state.failure_count += 1

        provider.state.last_error = error

        #
        # Circuit Breaker
        #

        if provider.state.failure_count >= 3:

            provider.state.disabled_until = (
                datetime.now(UTC)
                + timedelta(
                    minutes=10
                )
            )

    # ==========================================================
    # GET
    # ==========================================================

    def get(
        self,
        name: str,
    ) -> ProviderInfo:

        return self._providers[name]

    # ==========================================================
    # LIST
    # ==========================================================

    def list(self) -> list[ProviderInfo]:

        return list(self._providers.values())


provider_manager = ProviderManager()
