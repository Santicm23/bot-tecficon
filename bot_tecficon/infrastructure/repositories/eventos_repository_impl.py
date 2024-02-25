from typing import override

from ...domain.datasources import EventosDatasource
from ...domain.entities.evento import Evento
from ...domain.repositories.eventos_repository import EventosRepository


class EventosRepositoryImpl(EventosRepository):
    def __init__(self, datasource: EventosDatasource):
        self.datasource = datasource

    @override
    def get_eventos_by_siniestro(self, id_siniestro: int) -> list[Evento]:
        return self.datasource.get_eventos_by_siniestro(id_siniestro)

    @override
    def add_evento_to_siniestro(self, evento: Evento, id_siniestro: int) -> None:
        return self.datasource.add_evento_to_siniestro(evento, id_siniestro)
