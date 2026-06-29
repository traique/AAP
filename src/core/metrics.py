"""
AAP Core Metrics Engine

Thu thập số liệu runtime của Provider.
"""

from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter


@dataclass(slots=True)
class ProviderMetrics:
    """
    Runtime metrics của một Provider.
    """

    total_requests: int = 0

    successful_requests: int = 0

    failed_requests: int = 0

    total_latency: float = 0.0

    last_latency: float = 0.0

    def record_success(self, latency: float) -> None:
        self.total_requests += 1
        self.successful_requests += 1
        self.last_latency = latency
        self.total_latency += latency

    def record_failure(self, latency: float) -> None:
        self.total_requests += 1
        self.failed_requests += 1
        self.last_latency = latency
        self.total_latency += latency

    @property
    def success_rate(self) -> float:
        if self.total_requests == 0:
            return 1.0

        return self.successful_requests / self.total_requests

    @property
    def average_latency(self) -> float:
        if self.total_requests == 0:
            return 0.0

        return self.total_latency / self.total_requests


class MetricsEngine:
    """
    Quản lý metrics của toàn bộ Provider.
    """

    def __init__(self) -> None:
        self._metrics: dict[str, ProviderMetrics] = {}

    def get(self, provider_name: str) -> ProviderMetrics:
        return self._metrics.setdefault(
            provider_name,
            ProviderMetrics(),
        )

    def record_success(
        self,
        provider_name: str,
        latency: float,
    ) -> None:

        self.get(provider_name).record_success(latency)

    def record_failure(
        self,
        provider_name: str,
        latency: float,
    ) -> None:

        self.get(provider_name).record_failure(latency)


metrics_engine = MetricsEngine()


class Timer:
    """
    Context manager để đo latency.
    """

    def __enter__(self):
        self._start = perf_counter()
        return self

    def __exit__(self, *args):
        self.elapsed = perf_counter() - self._start
