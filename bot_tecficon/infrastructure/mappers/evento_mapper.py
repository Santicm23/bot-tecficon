
from typing import Any

from ...domain.entities import Evento


def sinapp_event_from_json(json: dict[str, Any]) -> Evento:
    return Evento(
        numero_siniestro=json['s.numero_siniestro'],
        fecha=json['e.fecha'],
        descripcion=json['e.descrip'],
        usuario_creacion=json['e.usuario_creacion'],
        notificar=json['e.notificar'],
    )


def sinapp_event_to_json(evento: Evento) -> dict[str, Any]:
    return {
        's.numero_siniestro': evento.numero_siniestro,
        'e.fecha': evento.fecha,
        'e.descrip': evento.descripcion,
        'e.usuario_creacion': evento.usuario_creacion,
        'e.notificar': evento.notificar,
    }
