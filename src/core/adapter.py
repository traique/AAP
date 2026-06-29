"""
AAP Base Adapter
"""

from __future__ import annotations

from abc import ABC


class Adapter(ABC):
    """
    Base class for every Adapter.
    """

    name: str = "unknown"

    version: str = "1.0.0"

    async def health(self) -> bool:
        """
        Check adapter health.
        """

        return True
