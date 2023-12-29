
from typing import override

from ...domain.datasources import SiniestrosDatasource
from ...domain.entities.siniestro import Siniestro
from ...domain.repositories import SiniestrosRepository


class SiniestrosRepositoryImpl(SiniestrosRepository):
    def __init__(self, datasource: SiniestrosDatasource):
        self.datasource = datasource

    @override
    def get_all_siniestros(self) -> list[Siniestro]:
        return self.datasource.get_all_siniestros()

    @override
    def get_siniestro_by_id(self, siniestro_id: int) -> Siniestro:
        return self.datasource.get_siniestro_by_id(siniestro_id)

    @override
    def add_siniestro(self, siniestro: Siniestro) -> None:
        return self.datasource.add_siniestro(siniestro)
