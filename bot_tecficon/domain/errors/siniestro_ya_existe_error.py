
from . import Error


class SiniestroYaExisteError(Error):
    def __init__(self, siniestro_id: int):
        super().__init__(f"El siniestro con id '{siniestro_id}' ya existe")
        self.siniestro_id = siniestro_id