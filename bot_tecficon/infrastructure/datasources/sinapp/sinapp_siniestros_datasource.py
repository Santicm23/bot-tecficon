
import json
from typing import override

import requests

from bot_tecficon.config.constants import environment

from ....domain.entities import Siniestro
from ....domain.datasources import SiniestrosDatasource


class SinappSiniestrosDatasource(SiniestrosDatasource):

    def __init__(self):
        self.url = 'http://10.8.0.1:8090/scriptcase/app/Hurtado_Gandini'
        self.session = requests.Session()
        self.session.params = {
            'tok': environment.TOK
        }

    @override
    def get_all_siniestros(self) -> list[Siniestro]:
        res = self.session.get(f'{self.url}/ep_lista_siniestros', timeout=5)

        data = res.text
        data = json.loads(data, strict=False)

        sinesters = data['data']

        return sinesters

    @override
    def get_siniestro_by_id(self, siniestro_id: int) -> Siniestro:
        ...

    @override
    def add_siniestro(self, siniestro: Siniestro) -> bool:
        ...
