import json
from typing import override

import requests

from ....config.constants import environment
from ....domain.datasources import VictimasDatasource
from ....domain.entities import Victima


class SinappVictimasDatasource(VictimasDatasource):
    def __init__(self):
        self.session = requests.Session()
        self.session.params = {"tok": environment.TOK}

    @override
    def get_victimas_by_siniestro(self, id_siniestro: int) -> list[Victima]:
        res = self.session.get(
            f"{environment.BASE_URL_SINAPP}/ep_ver_v_siniestros/", timeout=5
        )

        data = res.text
        data = json.loads(data, strict=False)

        raise

    @override
    def add_victima_to_siniestro(self, victima: Victima, id_siniestro: int) -> None:
        raise
