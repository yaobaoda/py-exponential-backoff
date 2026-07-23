"""Exponential backoff with full jitter. Standard library only."""
import random


def backoff_delay(attempt, base_ms=100, cap_ms=30_000, rng=random.random):
    """Delay in ms for a given 0-based attempt. Full jitter (AWS-style)."""
    if attempt < 0:
        raise ValueError("attempt must be >= 0")
    ceiling = min(cap_ms, base_ms * (2 ** attempt))
    return int(rng() * ceiling)
