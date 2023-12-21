
import json
from typing import override

import requests

from bot_tecficon.config.constants import environment
from bot_tecficon.domain.errors import SiniestroNoExisteError
from bot_tecficon.infrastructure.mappers import siniestro_mapper

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
            f'{environment.BASE_URL_SINAPP}/ep_lista_siniestros', timeout=5)

        data = res.text
        data = json.loads(data, strict=False)

        return [siniestro_mapper.sinapp_siniestro_from_json(json) for json in data['data']]

    @override
    def get_siniestro_by_id(self, siniestro_id: int) -> Siniestro:
        res = self.session.get(
            f'{environment.BASE_URL_SINAPP}/ep_ver_siniestro',
            params={'siniestro': siniestro_id},
            timeout=5
        )

        data = res.text
        data = json.loads(data, strict=False)

        if data['error'] is not None and len(data['error']) != 0:
            raise SiniestroNoExisteError(siniestro_id)

        return siniestro_mapper.sinapp_siniestro_from_json(data['data'][0])

    @override
    def add_siniestro(self, siniestro: Siniestro) -> bool:
        res = self.session.post(
            f'{environment.BASE_URL_SINAPP}/ep_crear_siniestro',
            data=siniestro_mapper.sinapp_siniestro_to_json(siniestro),
            timeout=5
        )

        data = res.text
        data = json.loads(data, strict=False)

        return res.status_code < 300
