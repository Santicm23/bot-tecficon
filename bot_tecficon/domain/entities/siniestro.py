from dataclasses import dataclass

"""
{
    "id_aseguradora":"1",
    "numero_siniestro":"899431242",
    "placa":"ZIK644",
    "fecha_asignacion_siniestro":"2023-12-4",
    "id_pais":"CO",
    "dpto":"antioquia",
    "ciudad":"medellin",
    "producto":"producto 1",
    "fecha_accidente":"2023-12-2",
    "direccion_ocurrencia":"direccion prueba",
    "tipo_encargo":"penal",
    "concepto_responsabilidad":"compartida",
    "lesiones":"Homicidio",
    "etapa_proceso_penal":"imputacion",
    "tramitador":"armando casas",
    "mediador":"sigigredo barrios",
    "tomador":"juan del mar",
    "propietario":"juan tamaris",
    "conductor_asegurado":"pepe perez",
    "informe_abogado":"este es el informe del abogado"
},
"""


@dataclass
class Siniestro:
    id_aseguradora: str
    numero_siniestro: str
    placa: str
    fecha_asignacion_siniestro: str
    ciudad: str
    dpto: str
    producto: str
    fecha_accidente: str
    direccion_ocurrencia: str
    tipo_encargo: str
    concepto_responsabilidad: str
    lesiones: str
    etapa_proceso_penal: str
    tramitador: str
    mediador: str
    tomador: str
    propietario: str
    conductor_asegurado: str
    informe_abogado: str
    id_pais: str
