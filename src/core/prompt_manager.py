"""
AAP Prompt Manager

Load and render Markdown prompt templates.
"""

from __future__ import annotations

import re
from pathlib import Path
from string import Template
from typing import Any


class PromptError(Exception):
    """Base prompt exception."""


class PromptNotFoundError(PromptError):
    """Prompt file does not exist."""


class PromptRenderError(PromptError):
    """Prompt rendering failed."""


_VARIABLE_PATTERN = re.compile(r"{{\s*([a-zA-Z0-9_]+)\s*}}")


class PromptManager:
    """
    Prompt template manager.

    Supports:

    - Markdown prompts
    - Cache
    - Variable rendering
    - Hot reload
    """

    def __init__(
        self,
        root: str | Path = "src/prompts",
    ) -> None:

        self._root = Path(root)

        self._cache: dict[str, str] = {}

    # ---------------------------------------------------------
    # Loading
    # ---------------------------------------------------------

    def load(
        self,
        name: str,
        *,
        use_cache: bool = True,
    ) -> str:

        if use_cache and name in self._cache:
            return self._cache[name]

        path = self._root / f"{name}.md"

        if not path.exists():
            raise PromptNotFoundError(
                f"Prompt '{name}' not found."
            )

        text = path.read_text(
            encoding="utf-8",
        )

        self._cache[name] = text

        return text

    # ---------------------------------------------------------
    # Rendering
    # ---------------------------------------------------------

    def render(
        self,
        name: str,
        **variables: Any,
    ) -> str:
        """
        Render prompt.

        Example:

            render(
                "chat",
                language="vi",
                history="...",
            )
        """

        prompt = self.load(name)

        #
        # Convert
        #
        # {{name}}
        #
        # ->
        #
        # ${name}
        #

        template = _VARIABLE_PATTERN.sub(
            lambda m: "${" + m.group(1) + "}",
            prompt,
        )

        try:

            return Template(template).substitute(
                {
                    key: "" if value is None else str(value)
                    for key, value in variables.items()
                }
            )

        except KeyError as exc:

            raise PromptRenderError(
                f"Missing variable: {exc.args[0]}"
            ) from exc

    # ---------------------------------------------------------
    # Cache
    # ---------------------------------------------------------

    def clear(self) -> None:

        self._cache.clear()

    def reload(
        self,
        name: str,
    ) -> str:

        self._cache.pop(name, None)

        return self.load(
            name,
            use_cache=False,
        )


prompt_manager = PromptManager()
