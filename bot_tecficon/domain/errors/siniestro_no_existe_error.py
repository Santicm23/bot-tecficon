
from . import Error


class SiniestroNoExisteError(Error):
    def __init__(self, siniestro_id: int, platform: str):
        super().__init__(f"El siniestro con id '{siniestro_id}' no existe en {platform}")
        self.siniestro_id = siniestro_id