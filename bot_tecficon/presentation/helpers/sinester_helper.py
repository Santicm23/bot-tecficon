
from ...infrastructure.datasources import SinappSiniestrosDatasource
from ...infrastructure.repositories import SiniestrosRepositoryImpl


def get_all_sinesters() -> list:
    siniestros_repository = SiniestrosRepositoryImpl(SinappSiniestrosDatasource())

    sinesters = siniestros_repository.get_siniestro_by_id("107431314")

    print(sinesters)

    return []
