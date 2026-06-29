"""
AAP Core Capabilities

Định nghĩa toàn bộ khả năng mà hệ thống hỗ trợ.
"""

from enum import Enum


class Capability(str, Enum):
    """
    Capability của Tool hoặc Provider.
    """

    # ===== Chat =====

    CHAT = "chat"

    # ===== Image =====

    IMAGE_GENERATION = "image_generation"

    IMAGE_EDIT = "image_edit"

    IMAGE_ANALYSIS = "image_analysis"

    # ===== Content =====

    CONTENT_WRITING = "content_writing"

    CONTENT_REWRITE = "content_rewrite"

    CONTENT_SUMMARY = "content_summary"

    # ===== Vision =====

    VISION = "vision"

    OCR = "ocr"

    # ===== Document =====

    DOCUMENT_CHAT = "document_chat"

    PDF = "pdf"

    WORD = "word"

    EXCEL = "excel"

    # ===== Search =====

    WEB_SEARCH = "web_search"

    NEWS = "news"

    # ===== Memory =====

    MEMORY_READ = "memory_read"

    MEMORY_WRITE = "memory_write"

    # ===== Utility =====

    TRANSLATE = "translate"

    CODE = "code"

    REASONING = "reasoning"

    # ===== Future =====

    AUDIO = "audio"

    VIDEO = "video"
