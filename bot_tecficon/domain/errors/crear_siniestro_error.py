from .error import Error


class CrearSiniestroError(Error):
    def __init__(self, siniestro_id: int, errors: list[str]):
        super().__init__(
            f"""El siniestro con id {siniestro_id} tiene atributos en Allianz que no corresponden con los de Sinapp:
            {', '.join(errors)}
            """
        )
        self.siniestro_id = siniestro_id
