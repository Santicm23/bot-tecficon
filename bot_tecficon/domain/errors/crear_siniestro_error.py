
from . import SiniestroError


class CrearSiniestroError(SiniestroError):
    def __init__(self, siniestro_id: int):
        super().__init__(f"El siniestro con id '{siniestro_id}' no se pudo crear")
        self.siniestro_id = siniestro_id