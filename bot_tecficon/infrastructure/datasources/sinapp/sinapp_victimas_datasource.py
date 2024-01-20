
from typing import override


from ....domain.entities import Victima
from ....domain.datasources import VictimasDatasource


class SinappVictimasDatasource(VictimasDatasource):

    @override
    def get_victimas_by_siniestro(self, id_siniestro: str) -> list[Victima]:
        raise

    @override
    def add_victima_to_siniestro(self, victima: Victima, id_siniestro: str) -> bool:
        raise
