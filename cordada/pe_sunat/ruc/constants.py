"""
RUC-related constants.
"""

from __future__ import annotations

import re


RUC_CANONICAL_STRICT_REGEX: re.Pattern
RUC_CANONICAL_STRICT_REGEX = re.compile(r'^(?P<digits>\d{10})(?P<check_digit>\d)$')
"""RUC (strict) regular expression for canonical format."""

RUC_CANONICAL_MAX_LENGTH = 11  # 10 + 1 = 2 + 8 + 1
"""RUC maximum length for canonical format."""

RUC_CANONICAL_MIN_LENGTH = 11
"""RUC minimum length for canonical format."""
