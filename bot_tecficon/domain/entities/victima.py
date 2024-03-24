from dataclasses import dataclass

"""
{
    "s.numero_siniestro": "107431314",
    "v.id_victima_sin": "2",
    "v.id_siniestro": "2",
    "v.nombre_victima": "Jader francisco medina",
    "v.telefono_victima": "3052344000",
    "v.apoderado_victima": "",
    "v.id_delito": "2",
    "v.id_despacho": "489",
    "v.id_juzgado": "",
    "v.id_estado_victima": "1",
    "v.id_etapa_proceso_civil": "",
    "v.id_pago": "2",
    "v.obs_abogado": "",
    "v.ult_valor_autorizado": "",
    "v.ult_valor_ofrecido_HYG": "",
    "v.valor_conciliado": "",
    "v.valor_estimado_conc": "",
    "v.valor_perdida_liquidada_por_HYG": "",
    "v.valor_pretension": "",
    "sincronizarfu": "N"
}
"""


@dataclass
class Victima:
    id_siniestro: int
    nombre: str
    telefono: str
    apoderado: str
    observacion_abogado: str
