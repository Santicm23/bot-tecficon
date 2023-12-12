
from typing import Any

from ...domain.entities import Siniestro


def sinester_from_json(json: dict[str, Any]) -> Siniestro:
    ...


def sinester_to_json(siniestro: Siniestro) -> dict[str, Any]:
    ...
