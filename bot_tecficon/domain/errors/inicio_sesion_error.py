
from . import Error


class InicioSesionError(Error):
    def __init__(self, platform: str):
        super().__init__(f'No se pudo iniciar sesión en la plataforma {platform}')
        self.platform = platform
