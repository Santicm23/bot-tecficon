
import time
from typing import override

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from ....config.constants import environment
from ....domain.errors import SiniestroNoExisteError
from ....infrastructure.mappers import siniestro_mapper
from ....domain.entities import Siniestro
from ....domain.datasources import SiniestrosDatasource


class IverosanSiniestrosDatasource(SiniestrosDatasource):
    def __init__(self):
        self.driver: webdriver.Chrome

    @override
    def get_all_siniestros(self) -> list[Siniestro]:
        raise

    @override
    def get_siniestro_by_id(self, siniestro_id: int) -> Siniestro:
        self.driver = webdriver.Chrome()

        # Login
        self.driver.get(environment.BASE_URL_ALLIA2)
        self.driver.set_window_size(968, 612)
        self.driver.find_element(By.ID, "nx-input-0").send_keys(environment.USER_ALLIA2)
        self.driver.find_element(By.ID, "nx-input-1").click()
        self.driver.find_element(By.ID, "nx-input-1").send_keys(environment.PASS_ALLIA2)
        self.driver.find_element(By.CSS_SELECTOR, ".nx-button__content-wrapper").click()
        time.sleep(5)

        # Entrar a página de siniestros
        element = self.driver.find_element(By.CSS_SELECTOR, ".c-main-navbar__link")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        time.sleep(2)
        subnavbar_el = self.driver.find_element(By.CSS_SELECTOR, ".c-subnavbar__item:nth-child(2) .c-subnavbar__title")
        actions.move_to_element(subnavbar_el).click().perform()
        time.sleep(2)
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.ID, "PENDING").click()

        # Buscar siniestro
        try:
            self.driver.find_element(By.XPATH, f"//*[contains(text(), '{siniestro_id}')]").click()
        except:
            # Si no existe el siniestro, cerrar el driver y lanzar excepción
            self.driver.quit()
            raise SiniestroNoExisteError(siniestro_id)

        placa = self.driver.find_element(By.ID, 'vehiclePlate').text
        fecha_asignacion_siniestro = self.driver.find_element(By.ID, 'orderDate').text
        ciudad = self.driver.find_element(By.ID, 'incidentCity').text
        dpto = self.driver.find_element(By.ID, 'incidentLocation_node1').text
        producto = self.driver.find_element(By.ID, 'productName').text
        fecha_accidente = self.driver.find_element(By.ID, 'incidentDate').text
        direccion_ocurrencia = self.driver.find_element(By.ID, 'incidentAddress').text
        tipo_encargo = self.driver.find_element(By.ID, 'orderTypeDesc').text
        concepto_responsabilidad = self.driver.find_element(By.ID, 'procInstaDesc').text # FIXME preguntar
        lesiones = self.driver.find_element(By.ID, 'orderTypeDesc').text
        etapa_proceso_penal = self.driver.find_element(By.ID, 'procInstaDesc').text # FIXME preguntar
        tramitador = self.driver.find_element(By.ID, 'tramitName').text
        mediador = self.driver.find_element(By.ID, 'agentName').text
        tomador = self.driver.find_element(By.ID, 'holderName').text
        propietario = self.driver.find_element(By.ID, 'ownerName').text
        conductor_asegurado = self.driver.find_element(By.ID, 'driverName').text
        informe_abogado = self.driver.find_element(By.ID, 'incidentVersion').text

        time.sleep(5)
        self.driver.quit()

        siniestro = Siniestro(
            numero_siniestro=str(siniestro_id),
            placa=placa,
            fecha_asignacion_siniestro=fecha_asignacion_siniestro,
            ciudad=ciudad,
            dpto=dpto,
            producto=producto,
            fecha_accidente=fecha_accidente,
            direccion_ocurrencia=direccion_ocurrencia,
            tipo_encargo=tipo_encargo,
            concepto_responsabilidad=concepto_responsabilidad,
            lesiones=lesiones,
            etapa_proceso_penal=etapa_proceso_penal,
            tramitador=tramitador,
            mediador=mediador,
            tomador=tomador,
            propietario=propietario,
            conductor_asegurado=conductor_asegurado,
            informe_abogado=informe_abogado
        )

        print(siniestro)

        return siniestro

    @override
    def add_siniestro(self, siniestro: Siniestro) -> bool:
        raise
