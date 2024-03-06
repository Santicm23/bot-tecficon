from .error import Error


class SiniestroNoAdmiteEventoError(Error):
    def __init__(self, siniestro_id: int):
        super().__init__(f"El siniestro con id {siniestro_id} no admite eventos.")
        self.siniestro_id = siniestro_id
