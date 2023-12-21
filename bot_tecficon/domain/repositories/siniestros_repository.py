
from abc import ABC, abstractmethod

from ..entities.siniestro import Siniestro


class SiniestrosRepository(ABC):

    @abstractmethod
    def get_all_siniestros(self) -> list[Siniestro]:
        ...
    
    @abstractmethod
    def get_siniestro_by_id(self, id_siniestro: int) -> dict:
        ...
    
    @abstractmethod
    def add_siniestro(self, siniestro: Siniestro) -> bool:
        ...
