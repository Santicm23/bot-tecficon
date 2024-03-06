from bot_tecficon.infrastructure.datasources.allianz.allianz_eventos_datasource import (
    AllianzEventosDatasource,
)

from ...infrastructure.datasources import (
    FollowUpEventosDatasource,
    SinappEventosDatasource,
    SinappSiniestrosDatasource,
)
from ...infrastructure.repositories import (
    EventosRepositoryImpl,
    SiniestrosRepositoryImpl,
)
from ..entities import Evento


def sincronizar_eventos(siniestro_id: int) -> None:
    sinapp_siniestros = SiniestrosRepositoryImpl(SinappSiniestrosDatasource())
    sinapp_siniestros.get_siniestro_by_id(
        siniestro_id
    )  # SiniestroNoExisteError if not found

    sinapp_eventos = EventosRepositoryImpl(SinappEventosDatasource())

    print(sinapp_eventos.get_eventos_by_siniestro(siniestro_id))
    # EventosRepositoryImpl(FollowUpEventosDatasource()).add_eventos_to_siniestro(
    EventosRepositoryImpl(AllianzEventosDatasource()).add_eventos_to_siniestro(
        [
            Evento(siniestro_id, "fecha", "descripcion", "CP301484", "notificar"),
            Evento(siniestro_id, "fecha2", "descripcion2", "CP301484", "notificar2"),
        ],
        siniestro_id,
    )
