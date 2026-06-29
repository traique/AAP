"""
AAP Gemini Client

Infrastructure wrapper around gemini-webapi.

This is the ONLY place in the project that knows about
the gemini_webapi package.
"""

from __future__ import annotations

from dataclasses import dataclass

from gemini_webapi import GeminiClient as WebGeminiClient
from gemini_webapi.types.modeloutput import ModelOutput

from utils.logger import logger


@dataclass(slots=True)
class GeminiResult:
    """
    Normalized Gemini response.
    """

    text: str

    images: list[bytes]

    videos: list[bytes]


class GeminiClient:
    """
    Thin wrapper around gemini-webapi.

    Responsibilities:
        - Initialize session
        - Call generate_content()
        - Health check
        - Close session

    This class MUST NOT:
        - Parse JSON
        - Know about Goal
        - Know about Planner
        - Know about Telegram
    """

    def __init__(
        self,
        *,
        psid: str,
        psidts: str | None = None,
    ) -> None:

        self._client = WebGeminiClient(
            psid,
            psidts,
        )

        self._initialized = False

    async def initialize(self) -> None:
        """
        Initialize Gemini session.
        """

        if self._initialized:
            return

        logger.info("Initializing Gemini client...")

        await self._client.init(
            timeout=60,
            auto_refresh=False,
        )

        self._initialized = True

        logger.info("Gemini client initialized.")

    async def generate(
        self,
        *,
        prompt: str,
    ) -> GeminiResult:
        """
        Generate content.
        """

        if not self._initialized:
            await self.initialize()

        response: ModelOutput = await self._client.generate_content(
            prompt
        )

        return GeminiResult(
            text=response.text or "",
            images=response.images,
            videos=response.videos,
        )

    async def health(self) -> bool:
        """
        Check whether Gemini session is alive.
        """

        try:

            if not self._initialized:
                await self.initialize()

            self._client.list_models()

            return True

        except Exception:

            logger.exception(
                "Gemini health check failed."
            )

            return False

    async def close(self) -> None:
        """
        Close HTTP session.
        """

        try:

            await self._client.close()

        except Exception:

            logger.exception(
                "Failed to close Gemini client."
              )
