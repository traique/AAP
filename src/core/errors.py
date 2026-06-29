"""
AAP Error Definitions
"""

from __future__ import annotations


class AAPError(Exception):
    """
    Base exception for AAP.
    """


# ==========================================================
# Runtime
# ==========================================================

class RuntimeError(AAPError):
    """Runtime execution error."""


class ExecutorError(RuntimeError):
    """Executor error."""


class PlannerError(RuntimeError):
    """Planner error."""


class ReasoningError(RuntimeError):
    """Reasoning error."""


# ==========================================================
# Provider
# ==========================================================

class ProviderError(AAPError):
    """Provider error."""


class ProviderNotFoundError(ProviderError):
    """No provider available."""


class ProviderUnavailableError(ProviderError):
    """Provider temporarily unavailable."""


class ProviderTimeoutError(ProviderError):
    """Provider timeout."""


class ProviderAuthenticationError(ProviderError):
    """Provider authentication failed."""


# ==========================================================
# Tool
# ==========================================================

class ToolError(AAPError):
    """Tool error."""


class ToolNotFoundError(ToolError):
    """Tool not found."""


class ToolExecutionError(ToolError):
    """Tool execution failed."""


# ==========================================================
# Prompt
# ==========================================================

class PromptError(AAPError):
    """Prompt error."""


class PromptNotFoundError(PromptError):
    """Prompt file not found."""


class PromptRenderError(PromptError):
    """Prompt render failed."""


# ==========================================================
# JSON
# ==========================================================

class JsonParseError(AAPError):
    """Invalid JSON returned by LLM."""


# ==========================================================
# Validation
# ==========================================================

class ValidationError(AAPError):
    """Validation failed."""
