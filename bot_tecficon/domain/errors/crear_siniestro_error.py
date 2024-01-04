
from . import Error


class CrearSiniestroError(Error):
    def __init__(self, siniestro_id: int):
        super().__init__(
            f"""El siniestro con id {siniestro_id} tiene atributos en Allianz que no corresponden con los de Sinapp,
                por favor, corrijalos o haga el procedimiento manualmente.""")
        self.siniestro_id = siniestro_id
