"""
AI Assistant Platform (AAP)

core/context.py

Shared execution context.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class UserContext:
    """
    User information.
    """

    id: int

    username: str | None = None

    full_name: str | None = None

    language: str = "vi"


@dataclass(slots=True)
class ChatContext:
    """
    Chat information.
    """

    id: int

    type: str = "private"


@dataclass(slots=True)
class SessionContext:
    """
    One conversation session.
    """

    id: str

    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass(slots=True)
class MemoryContext:
    """
    Long-term memory.

    Example:

    {
        "name": "Minh",
        "job": "Real Estate",
        "style": "Professional"
    }
    """

    values: dict[str, Any] = field(default_factory=dict)

    def get(self, key: str, default: Any = None):

        return self.values.get(key, default)

    def set(self, key: str, value: Any):

        self.values[key] = value

    def remove(self, key: str):

        self.values.pop(key, None)


@dataclass(slots=True)
class RequestContext:
    """
    Runtime context.

    Shared across the entire execution pipeline.
    """

    request_id: str

    user: UserContext

    chat: ChatContext

    session: SessionContext

    memory: MemoryContext = field(default_factory=MemoryContext)

    metadata: dict[str, Any] = field(default_factory=dict)

    def set(self, key: str, value: Any):

        self.metadata[key] = value

    def get(self, key: str, default: Any = None):

        return self.metadata.get(key, default)"""
AI Assistant Platform (AAP)

core/context.py

Shared execution context.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class UserContext:
    """
    User information.
    """

    id: int

    username: str | None = None

    full_name: str | None = None

    language: str = "vi"


@dataclass(slots=True)
class ChatContext:
    """
    Chat information.
    """

    id: int

    type: str = "private"


@dataclass(slots=True)
class SessionContext:
    """
    One conversation session.
    """

    id: str

    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass(slots=True)
class MemoryContext:
    """
    Long-term memory.

    Example:

    {
        "name": "Minh",
        "job": "Real Estate",
        "style": "Professional"
    }
    """

    values: dict[str, Any] = field(default_factory=dict)

    def get(self, key: str, default: Any = None):

        return self.values.get(key, default)

    def set(self, key: str, value: Any):

        self.values[key] = value

    def remove(self, key: str):

        self.values.pop(key, None)


@dataclass(slots=True)
class RequestContext:
    """
    Runtime context.

    Shared across the entire execution pipeline.
    """

    request_id: str

    user: UserContext

    chat: ChatContext

    session: SessionContext

    memory: MemoryContext = field(default_factory=MemoryContext)

    metadata: dict[str, Any] = field(default_factory=dict)

    def set(self, key: str, value: Any):

        self.metadata[key] = value

    def get(self, key: str, default: Any = None):

        return self.metadata.get(key, default)
