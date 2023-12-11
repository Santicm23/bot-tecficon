
import os
import json

import requests


def get_all_sinesters() -> list:
    """Get all sinesters from database"""

    baseurl = 'http://10.8.0.1:8090/scriptcase/app/Hurtado_Gandini'
    tok = os.getenv('TOK')

    res = requests.get(
        f'{baseurl}/ep_lista_siniestros', params={'tok': tok}, timeout=5)

    data = res.text
    data = json.loads(data, strict=False)

    sinesters = data['data']

    return sinesters
