
import json
from typing import override

import requests

from bot_tecficon.config.constants import environment
from bot_tecficon.infrastructure.mappers.siniestro_mapper import sinapp_siniestro_from_json

from ....domain.entities import Siniestro
from ....domain.datasources import SiniestrosDatasource


class SinappSiniestrosDatasource(SiniestrosDatasource):

    def __init__(self):
        self.session = requests.Session()
        self.session.params = {
            'tok': environment.TOK
        }

    @override
    def get_all_siniestros(self) -> list[Siniestro]:
        res = self.session.get(
            f'{environment.BASE_URL}/ep_lista_siniestros', timeout=5)

        data = res.text
        data = json.loads(data, strict=False)

        return [sinapp_siniestro_from_json(json) for json in data['data']]

    @override
    def get_siniestro_by_id(self, siniestro_id: int) -> Siniestro:
        res = self.session.get(
            f'{environment.BASE_URL}/ep_ver_siniestro',
            params={'siniestro': siniestro_id},
            timeout=5
        )

        data = res.text
        data = json.loads(data, strict=False)

        return sinapp_siniestro_from_json(data['data'][0])

    @override
    def add_siniestro(self, siniestro: Siniestro) -> bool:
        ...
