from ...infrastructure.datasources.follow_up.follow_up_eventos_datasource import (
    FollowUpEventosDatasource,
)
from ...infrastructure.repositories import EventosRepositoryImpl
from ..entities import Evento


def sincronizar_eventos(siniestro_id: int) -> None:
    EventosRepositoryImpl(FollowUpEventosDatasource()).add_evento_to_siniestro(
        Evento(siniestro_id, "", "", "", ""), siniestro_id
    )
