
from abc import ABC, abstractmethod

from ..entities.victima import Victima


class VictimasRepository(ABC):

    @abstractmethod
    def get_victimas_by_siniestro(self, id_siniestro: str) -> list[Victima]:
        ...

    @abstractmethod
    def add_victima_to_siniestro(self, victima: Victima, id_siniestro: str) -> bool:
        ...
