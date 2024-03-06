from abc import ABC, abstractmethod

from ..entities.evento import Evento


class EventosRepository(ABC):
    @abstractmethod
    def get_eventos_by_siniestro(self, id_siniestro: int) -> list[Evento]: ...

    @abstractmethod
    def add_eventos_to_siniestro(
        self, eventos: list[Evento], id_siniestro: int
    ) -> None: ...
