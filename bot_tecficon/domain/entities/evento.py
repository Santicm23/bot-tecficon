from dataclasses import dataclass

"""
{
    "s.numero_siniestro": "82459275",
    "e.id_evento_sin": "1",
    "e.id_siniestro": "183",
    "e.id_tipo_evento": "2",
    "e.fecha": "2023-02-20",
    "e.descrip": "Hoy tuvimos contacto con apoderado de victima. ",
    "e.usuario_creacion": "[usr_login]",
    "e.notificar": "N",
    "e.a_quien_notifica": "",
    "sincronizarfu": "N",
    "sincronizarib": "N"
}
"""


@dataclass
class Evento:
    numero_siniestro: int
    fecha: str
    descripcion: str
    usuario_creacion: str
    notificar: str
