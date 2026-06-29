"""
AAP JSON Parser

Utility functions for extracting JSON from LLM responses.
"""

from __future__ import annotations

import json
import re
from typing import Any


class JsonParseError(ValueError):
    """
    Raised when valid JSON cannot be extracted.
    """


_CODE_BLOCK_PATTERN = re.compile(
    r"```(?:json)?\s*(.*?)```",
    re.IGNORECASE | re.DOTALL,
)


def clean_markdown(text: str) -> str:
    """
    Remove markdown code fences if present.

    Example:

    ```json
    {...}
    ```

    ->
    {...}
    """

    text = text.strip()

    match = _CODE_BLOCK_PATTERN.search(text)

    if match:
        return match.group(1).strip()

    return text


def extract_json_text(text: str) -> str:
    """
    Extract the first complete JSON object or array.

    Works even when the LLM adds explanations
    before or after the JSON.
    """

    text = clean_markdown(text)

    start = None
    opening = None

    for i, ch in enumerate(text):
        if ch in "{[":
            start = i
            opening = ch
            break

    if start is None:
        raise JsonParseError("No JSON found.")

    closing = "}" if opening == "{" else "]"

    depth = 0

    for i in range(start, len(text)):

        ch = text[i]

        if ch == opening:
            depth += 1

        elif ch == closing:
            depth -= 1

            if depth == 0:
                return text[start : i + 1]

    raise JsonParseError("Incomplete JSON.")


def parse_json(text: str) -> Any:
    """
    Parse any JSON value.

    Returns:

    - dict
    - list
    - str
    - int
    - float
    - bool
    """

    json_text = extract_json_text(text)

    try:
        return json.loads(json_text)

    except json.JSONDecodeError as exc:

        raise JsonParseError(
            f"Invalid JSON: {exc}"
        ) from exc


def parse_json_object(text: str) -> dict[str, Any]:
    """
    Parse JSON object.

    Raises if result is not an object.
    """

    data = parse_json(text)

    if not isinstance(data, dict):

        raise JsonParseError(
            "Expected JSON object."
        )

    return data


def parse_json_array(text: str) -> list[Any]:
    """
    Parse JSON array.

    Raises if result is not an array.
    """

    data = parse_json(text)

    if not isinstance(data, list):

        raise JsonParseError(
            "Expected JSON array."
        )

    return data
