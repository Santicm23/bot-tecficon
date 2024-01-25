from ...infrastructure.datasources.follow_up.follow_up_eventos_datasource import (
    FollowUpEventosDatasource,
)
from ...infrastructure.repositories import EventosRepositoryImpl


def sincronizar_eventos(siniestro_id: int) -> None:
    EventosRepositoryImpl(FollowUpEventosDatasource()).get_eventos_by_siniestro(
        siniestro_id
    )
