from __future__ import annotations


def make_safe_name(name: str) -> str:
    return name.lower().strip().replace(" ", "_")
