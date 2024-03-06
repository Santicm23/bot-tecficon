from .error import Error


class NoHayEventosError(Error):
    def __init__(self, siniestro_id: int):
        super().__init__(f"El siniestro con id {siniestro_id} no tiene eventos")
        self.siniestro_id = siniestro_id
