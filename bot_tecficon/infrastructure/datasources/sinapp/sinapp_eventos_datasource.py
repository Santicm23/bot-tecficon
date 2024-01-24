
import json
from typing import override

import requests

from ...mappers import evento_mapper
from ....config.constants import environment
from ....domain.datasources import EventosDatasource
from ....domain.entities import Evento


class SinappEventosDatasource(EventosDatasource):

    def __init__(self):
        self.session = requests.Session()
        self.session.params = {
            'tok': environment.TOK
        }
    
    @override
    def get_eventos_by_siniestro(self, id_siniestro: int) -> list[Evento]:
        res = self.session.get(
            f'{environment.BASE_URL_SINAPP}/ep_ver_e_siniestro/', timeout=5, params={'siniestro': id_siniestro})

        data = res.text
        data = json.loads(data, strict=False)

        return [evento_mapper.sinapp_event_from_json(json) for json in data['data']]

    @override
    def add_evento_to_siniestro(self, evento: Evento, id_siniestro: int) -> bool:
        ...