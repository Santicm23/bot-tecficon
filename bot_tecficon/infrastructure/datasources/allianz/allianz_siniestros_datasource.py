
import time
from typing import override

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from .login import login_allianz
from ....domain.datasources import SiniestrosDatasource
from ....domain.entities import Siniestro
from ....domain.errors import SeleniumError, SiniestroNoExisteError


class AllianzSiniestrosDatasource(SiniestrosDatasource):
    def __init__(self):
        self.driver: webdriver.Chrome

    def str_optional_to_str(self, str_optional: str | None) -> str:
        return str_optional if str_optional else ''

    def format_date(self, date: str) -> str:
        date_split = date.split('/')
        date_split.reverse()
        return f'{date_split[0]}-{date_split[1]}-{date_split[2]}'

    def read_sinester_selenium(self, id_siniestro: int) -> Siniestro:
        self.driver = webdriver.Chrome()

        login_allianz(self.driver)

        # Buscar siniestro
        try:
            self.driver.find_element(
                By.XPATH, f"//*[contains(text(), '{id_siniestro}')]").click()
        except:
            # Si no existe el siniestro, cerrar el driver y lanzar excepción
            self.driver.quit()
            raise SiniestroNoExisteError(id_siniestro, 'Allianz')

        placa = self.driver.find_element(
            By.ID, 'vehiclePlate').get_attribute('value')

        fecha_asignacion_siniestro = self.str_optional_to_str(self.driver.find_element(
            By.ID, 'orderDate').get_attribute('value'))

        fecha_asignacion_siniestro = self.format_date(
            fecha_asignacion_siniestro)

        ciudad = self.driver.find_element(
            By.ID, 'incidentCity').get_attribute('value')

        dpto = Select(self.driver.find_element(
            By.ID, 'incidentLocation_node1'))
        dpto = dpto.first_selected_option.text

        producto = self.driver.find_element(
            By.ID, 'productName').get_attribute('value')

        fecha_accidente = self.str_optional_to_str(self.driver.find_element(
            By.ID, 'incidentDate').get_attribute('value'))

        fecha_accidente = self.format_date(fecha_accidente)

        direccion_ocurrencia = self.driver.find_element(
            By.ID, 'incidentAddress').get_attribute('value')

        tipo_encargo = self.driver.find_element(
            By.ID, 'procTypeDesc').get_attribute('value')

        tipo_encargo = tipo_encargo.lower() if tipo_encargo else ''

        desc_instancia_procedimiento = self.str_optional_to_str(self.driver.find_element(
            By.ID, 'procInstaDesc').get_attribute('value')).split(' - ')

        etapa_proceso_penal = desc_instancia_procedimiento[0]

        concepto_responsabilidad = (
            'Evidente'
        ) if 'con' in desc_instancia_procedimiento[1].lower() else (
            'Inexistente'
        )  # FIXME preguntar

        lesiones = self.driver.find_element(
            By.ID, 'orderTypeDesc').get_attribute('value')

        tramitador = self.driver.find_element(
            By.ID, 'tramitName').get_attribute('value')

        mediador = self.driver.find_element(
            By.ID, 'agentName').get_attribute('value')

        tomador = self.driver.find_element(
            By.ID, 'holderName').get_attribute('value')

        propietario = self.driver.find_element(
            By.ID, 'ownerName').get_attribute('value')

        conductor_asegurado = self.driver.find_element(
            By.ID, 'driverName').get_attribute('value')

        informe_abogado = self.driver.find_element(
            By.ID, 'incidentVersion').get_attribute('value')

        time.sleep(5)
        self.driver.quit()

        siniestro = Siniestro(
            numero_siniestro=str(id_siniestro),
            placa=self.str_optional_to_str(placa),
            fecha_asignacion_siniestro=fecha_asignacion_siniestro,
            ciudad=self.str_optional_to_str(ciudad),
            dpto=dpto,
            producto=self.str_optional_to_str(producto),
            fecha_accidente=fecha_accidente,
            direccion_ocurrencia=self.str_optional_to_str(
                direccion_ocurrencia),
            tipo_encargo=self.str_optional_to_str(tipo_encargo),
            concepto_responsabilidad=concepto_responsabilidad,
            lesiones=self.str_optional_to_str(lesiones),
            etapa_proceso_penal=etapa_proceso_penal,
            tramitador=self.str_optional_to_str(tramitador),
            mediador=self.str_optional_to_str(mediador),
            tomador=self.str_optional_to_str(tomador),
            propietario=self.str_optional_to_str(propietario),
            conductor_asegurado=self.str_optional_to_str(conductor_asegurado),
            informe_abogado=self.str_optional_to_str(informe_abogado),
            id_aseguradora='1',
            id_pais='CO'
        )

        return siniestro

    @override
    def get_all_siniestros(self) -> list[Siniestro]:
        raise

    @override
    def get_siniestro_by_id(self, id_siniestro: int) -> Siniestro:
        try:
            return self.read_sinester_selenium(id_siniestro)
        except SiniestroNoExisteError as e:
            raise e
        except Exception:
            raise SeleniumError()

    @override
    def add_siniestro(self, siniestro: Siniestro) -> None:
        raise
