"""Timestamp formatting utilities.

All exported second values must have exactly 3 decimal places.
"""

from decimal import Decimal, ROUND_HALF_UP

THREE_DP_QUANT = Decimal("0.001")


def format_seconds(value: float | int | Decimal) -> str:
    """Format seconds with exactly 3 decimal places."""
    decimal_value = Decimal(str(value)).quantize(THREE_DP_QUANT, rounding=ROUND_HALF_UP)
    return f"{decimal_value:.3f}"


def parse_seconds(value: str) -> float:
    """Parse a seconds string back to float."""
    return float(value)
