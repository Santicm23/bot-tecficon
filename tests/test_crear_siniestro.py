
from bot_tecficon.domain.use_cases import crear_siniestro, siniestro_existe
    

def test_crear_siniestro() -> None:

    id_siniestro = 134711028

    crear_siniestro(id_siniestro)

    assert siniestro_existe(id_siniestro) is True
