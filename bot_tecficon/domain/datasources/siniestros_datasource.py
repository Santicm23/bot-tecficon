
from abc import ABC, abstractmethod

from ..entities.siniestro import Siniestro


class SiniestrosDatasource(ABC):

    @abstractmethod
    def get_all_siniestros(self) -> list[Siniestro]:
        ...

    @abstractmethod
    def get_siniestro_by_id(self, id_siniestro: int) -> Siniestro:
        ...

    @abstractmethod
    def add_siniestro(self, siniestro: Siniestro) -> None:
        ...
