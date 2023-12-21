
from ..errors import SiniestroNoExisteError
from ...infrastructure.datasources import SinappSiniestrosDatasource
from ...infrastructure.repositories import SiniestrosRepositoryImpl


__repository_sinapp = SiniestrosRepositoryImpl(SinappSiniestrosDatasource())
__repository_iverosan = SiniestrosRepositoryImpl(SinappSiniestrosDatasource()) #TODO: corregir nombre de la segunda app

def siniestro_existe(siniestro_id: int) -> bool:
    try:
        __repository_sinapp.get_siniestro_by_id(siniestro_id)
    except SiniestroNoExisteError:
        return False

    return True


def crear_sinistro(siniestro_id: int) -> str:
    '''Crea un siniestro en SINAPP a partir de IVEROSAN''' #TODO: corregir nombre de la segunda app
    
    if siniestro_existe(siniestro_id):
        return 'El siniestro ya existe'
    
    siniestro = __repository_iverosan.get_siniestro_by_id(siniestro_id)
    
    __repository_sinapp.add_siniestro(siniestro)

    return 'El siniestro se ha creado correctamente'
