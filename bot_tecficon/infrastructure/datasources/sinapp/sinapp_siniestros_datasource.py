import json
from typing import override

import requests

from ....config.constants import environment
from ....domain.datasources import SiniestrosDatasource
from ....domain.entities import Siniestro
from ....domain.errors import CrearSiniestroError, SiniestroNoExisteError
from ....infrastructure.mappers import siniestro_mapper


class SinappSiniestrosDatasource(SiniestrosDatasource):

    def __init__(self):
        self.session = requests.Session()
        self.session.params = {"tok": environment.TOK}

    @override
    def get_all_siniestros(self) -> list[Siniestro]:
        res = self.session.get(
            f"{environment.BASE_URL_SINAPP}/ep_lista_siniestros/", timeout=5
        )

        data = res.text
        data = json.loads(data, strict=False)

        return [
            siniestro_mapper.sinapp_siniestro_from_json(json) for json in data["data"]
        ]

    @override
    def get_siniestro_by_id(self, id_siniestro: int) -> Siniestro:
        res = self.session.get(
            f"{environment.BASE_URL_SINAPP}/ep_ver_siniestro/",
            params={"siniestro": id_siniestro},
            timeout=5,
        )

        data = res.text
        data = json.loads(data, strict=False)

        if data["error"] is not None and len(data["error"]) != 0:
            raise SiniestroNoExisteError(id_siniestro, "Sinapp")

        return siniestro_mapper.sinapp_siniestro_from_json(data["data"][0])

    @override
    def add_siniestro(self, siniestro: Siniestro) -> None:
        send_json = siniestro_mapper.sinapp_siniestro_to_json(siniestro)
        print(send_json)
        res = self.session.post(
            f"{environment.BASE_URL_SINAPP}/ep_crear_siniestro/",
            data=json.dumps(send_json),
            timeout=5,
        )

        data = res.text
        data = json.loads(data, strict=False)

        if "Excepciones" in data and len(data["error"]) != 0:
            raise CrearSiniestroError(int(siniestro.numero_siniestro), data["error"])
