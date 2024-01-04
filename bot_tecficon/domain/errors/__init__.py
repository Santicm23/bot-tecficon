from .error import Error
from .siniestro_no_existe_error import SiniestroNoExisteError
from .crear_siniestro_error import CrearSiniestroError
from .siniestro_ya_existe_error import SiniestroYaExisteError
from .selenium_error import SeleniumError

__all__ = [
    'Error',
    'SiniestroNoExisteError',
    'CrearSiniestroError',
    'SiniestroYaExisteError',
    'SeleniumError'
]
