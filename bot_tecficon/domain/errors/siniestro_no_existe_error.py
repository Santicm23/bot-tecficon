
from . import Error


class SiniestroNoExisteError(Error):
    def __init__(self, siniestro_id: int):
        super().__init__(f"El siniestro con id '{siniestro_id}' no existe")
        self.siniestro_id = siniestro_id