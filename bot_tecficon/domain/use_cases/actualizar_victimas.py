from ...infrastructure.datasources import FollowUpVictimasDatasource
from ...infrastructure.repositories import VictimasRepositoryImpl
from ..entities import Victima


def actualizar_victimas(siniestro_id: int) -> None:
    repository = VictimasRepositoryImpl(FollowUpVictimasDatasource())

    repository.add_victima_to_siniestro(Victima(), siniestro_id)
