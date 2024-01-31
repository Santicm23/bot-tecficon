from typing import override

from ....domain.datasources import VictimasDatasource
from ....domain.entities import Victima


class SinappVictimasDatasource(VictimasDatasource):
    @override
    def get_victimas_by_siniestro(self, id_siniestro: str) -> list[Victima]:
        raise

    @override
    def add_victima_to_siniestro(self, victima: Victima, id_siniestro: str) -> None:
        raise
