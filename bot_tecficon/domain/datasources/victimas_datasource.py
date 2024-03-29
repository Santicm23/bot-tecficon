from abc import ABC, abstractmethod

from ..entities.victima import Victima


class VictimasDatasource(ABC):
    @abstractmethod
    def get_victimas_by_siniestro(self, id_siniestro: int) -> list[Victima]: ...

    @abstractmethod
    def add_victima_to_siniestro(self, victima: Victima, id_siniestro: int) -> None: ...
