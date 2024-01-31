from ...infrastructure.datasources import (  # FollowUpEventosDatasource,
    AllianzEventosDatasource,
)
from ...infrastructure.repositories import EventosRepositoryImpl
from ..entities import Evento


def sincronizar_eventos(siniestro_id: int) -> None:
    # EventosRepositoryImpl(FollowUpEventosDatasource()).add_evento_to_siniestro(
    EventosRepositoryImpl(AllianzEventosDatasource()).add_evento_to_siniestro(
        Evento(siniestro_id, "fecha", "descripcion", "CP301484", "notificar"),
        siniestro_id,
    )
