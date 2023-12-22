
from bot_tecficon.domain.entities.siniestro import Siniestro
from ...infrastructure.datasources import SinappSiniestrosDatasource
from ...infrastructure.repositories import SiniestrosRepositoryImpl


siniestros_repository = SiniestrosRepositoryImpl(SinappSiniestrosDatasource())


def get_all_sinesters() -> list[Siniestro]:
    return siniestros_repository.get_all_siniestros()


def get_sinester_by_id(id: int) -> Siniestro:
    return siniestros_repository.get_siniestro_by_id(id)

def add_sineter(sinester: Siniestro) -> bool:
    return siniestros_repository.add_siniestro(sinester)
