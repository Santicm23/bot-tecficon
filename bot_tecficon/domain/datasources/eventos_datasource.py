
from abc import ABC, abstractmethod

from ..entities.evento import Evento


class EventosDatasource(ABC):

    @abstractmethod
    def get_eventos_by_siniestro(self, id_siniestro: int) -> list[Evento]:
        ...

    @abstractmethod
    def add_evento_to_siniestro(self, evento: Evento, id_siniestro: int) -> bool:
        ...
