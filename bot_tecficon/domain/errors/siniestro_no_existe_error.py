
from . import SiniestroError


class SiniestroNoExisteError(SiniestroError):
    def __init__(self, siniestro_id: int):
        super().__init__(f"El siniestro {siniestro_id} no existe")
        self.siniestro_id = siniestro_id