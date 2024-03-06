import time
from typing import override

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from ....domain.datasources import EventosDatasource
from ....domain.entities import Evento
from .login import login_allianz


class AllianzEventosDatasource(EventosDatasource):
    def __init__(self):
        self.driver: webdriver.Chrome

    @override
    def get_eventos_by_siniestro(self, id_siniestro: int) -> list[Evento]:
        self.driver = webdriver.Chrome()

        login_allianz(self.driver)

        self.driver.close()

        return []

    @override
    def add_eventos_to_siniestro(
        self, eventos: list[Evento], id_siniestro: int
    ) -> None:
        self.driver = webdriver.Chrome()

        login_allianz(self.driver)

        self.driver.find_element(By.ID, "claimNumber").send_keys(id_siniestro)
        self.driver.find_element(By.ID, "claimNumber").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "o_10").click()

        self.driver.find_element(By.ID, "row_0_ordersList").click()

        self.driver.find_element(By.ID, "FG").click()

        self.driver.switch_to.window(self.driver.window_handles[1])

        time.sleep(12)

        for evento in eventos:
            self.driver.find_element(By.ID, "0").click()

            time.sleep(10)

            self.driver.find_element(By.ID, "codigo").send_keys(evento.modelo)

            # ? Preguntar que se pone en este campo
            # self.driver.find_element(By.ID, "litModelo").send_keys("No se")

            self.driver.find_element(By.ID, "texto").send_keys(evento.descripcion)

            self.driver.find_element(
                By.XPATH, f"//*[contains(text(), 'Atrás')]"
            ).click()
            # self.driver.find_element(By.XPATH, f"//*[contains(text(), 'Grabar')]").click()

            time.sleep(5)

        self.driver.close()
