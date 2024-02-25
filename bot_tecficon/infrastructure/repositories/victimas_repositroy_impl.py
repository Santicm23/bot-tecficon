from typing import override

from ...domain.datasources import VictimasDatasource
from ...domain.entities import Victima
from ...domain.repositories import VictimasRepository


class VictimasRepositoryImpl(VictimasRepository):
    def __init__(self, datasource: VictimasDatasource):
        self.datasource = datasource

    @override
    def get_victimas_by_siniestro(self, id_siniestro: int) -> list[Victima]:
        return self.datasource.get_victimas_by_siniestro(id_siniestro)

    @override
    def add_victima_to_siniestro(self, victima: Victima, id_siniestro: int) -> None:
        return self.datasource.add_victima_to_siniestro(victima, id_siniestro)
