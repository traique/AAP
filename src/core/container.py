"""
AAP Dependency Injection Container
"""

from __future__ import annotations

from typing import Any, TypeVar

T = TypeVar("T")


class ServiceNotFoundError(KeyError):
    """
    Raised when a service is not registered.
    """


class Container:
    """
    Simple Dependency Injection Container.
    """

    def __init__(self) -> None:

        self._services: dict[type[Any], Any] = {}

    def register(
        self,
        interface: type[T],
        instance: T,
    ) -> None:
        """
        Register a singleton instance.
        """

        self._services[interface] = instance

    def resolve(
        self,
        interface: type[T],
    ) -> T:
        """
        Resolve a service.
        """

        try:
            return self._services[interface]

        except KeyError as exc:
            raise ServiceNotFoundError(
                f"Service '{interface.__name__}' not registered."
            ) from exc

    def contains(
        self,
        interface: type[Any],
    ) -> bool:
        """
        Check whether a service is registered.
        """

        return interface in self._services

    def clear(self) -> None:
        """
        Remove all registered services.
        """

        self._services.clear()


container = Container()
