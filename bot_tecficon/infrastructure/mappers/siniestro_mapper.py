
from typing import Any

from ...domain.entities import Siniestro


def sinapp_siniestro_from_json(json: dict[str, Any]) -> Siniestro:
    return Siniestro(
        numero_siniestro=json["numero_siniestro"],
        placa=json["placa"],
        ciudad=json["id_ciudad"],
        concepto_responsabilidad=json["id_concepto_responsabilidad"],
        conductor_asegurado=json["nombre_conductor_asegurado"],
        direccion_ocurrencia=json["lugar_direccion_ocurrencia"],
        dpto=json["id_dpto"],
        etapa_proceso_penal=json["id_etapa_proceso_penal"],
        fecha_accidente=json["fecha_accidente"],
        fecha_asignacion_siniestro=json["fecha_aceptacion_encargo"],
        informe_abogado="",
        lesiones=json["lesiones"],
        mediador=json["mediador"],
        producto=json["producto"],
        propietario=json["nombre_propietario"],
        tipo_encargo=json["id_tipo_encargo"],
        tomador=json["nombre_tomador"],
        tramitador=json["tramitador"],
        id_aseguradora=json["id_aseguradora"],
        id_pais=json["id_pais"]
    )


def sinapp_siniestro_to_json(siniestro: Siniestro) -> dict[str, Any]:
    return siniestro.__dict__
