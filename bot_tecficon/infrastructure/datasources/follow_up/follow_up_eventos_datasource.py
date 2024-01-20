
from typing import override

from selenium import webdriver

from ....domain.datasources import EventosDatasource
from ....domain.entities import Evento


class FollowUpEventosDatasource(EventosDatasource):
    def __init__(self):
        self.driver: webdriver.Chrome

    @override
    def get_eventos_by_siniestro(self, id_siniestro: str) -> list[Evento]:
        ...

    @override
    def add_evento_to_siniestro(self, evento: Evento, id_siniestro: str) -> bool:
        ...
