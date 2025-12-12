"""JSON formatter for structured search results."""
import json
from typing import Any, Dict


def format_json(result: Dict[str, Any]) -> str:
    """Return a JSON string for the structured result.

    Uses indent for readability and ensures all data is serializable.
    """
    return json.dumps(result, indent=2, ensure_ascii=False)
