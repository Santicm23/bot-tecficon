
from .error import Error


class SiniestroYaExisteError(Error):
    def __init__(self, siniestro_id: int, platform: str):
        super().__init__(f"El siniestro con id '{
            siniestro_id}' ya existe en {platform}")
        self.siniestro_id = siniestro_id
