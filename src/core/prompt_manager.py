"""
AAP Prompt Manager

Load prompt templates from the prompts directory.
"""

from __future__ import annotations

from pathlib import Path


class PromptNotFoundError(FileNotFoundError):
    """
    Prompt file not found.
    """


class PromptManager:
    """
    Load prompts from Markdown files.
    """

    def __init__(
        self,
        root: str | Path = "src/prompts",
    ) -> None:

        self._root = Path(root)

        self._cache: dict[str, str] = {}

    def load(
        self,
        name: str,
        *,
        use_cache: bool = True,
    ) -> str:
        """
        Load a prompt.

        Example:
            load("reasoner")
        """

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

    def clear_cache(self) -> None:
        """
        Clear prompt cache.
        """

        self._cache.clear()


prompt_manager = PromptManager()
