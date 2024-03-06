import time
from typing import override

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from ....domain.datasources import EventosDatasource
from ....domain.entities import Evento
from .login import login_follow_up


class FollowUpEventosDatasource(EventosDatasource):
    def __init__(self):
        self.driver: webdriver.Chrome

    @override
    def get_eventos_by_siniestro(self, id_siniestro: int) -> list[Evento]:
        self.driver = webdriver.Chrome()

        login_follow_up(self.driver)

        input_filter = self.driver.find_element(By.ID, "newdefaultfilter")
        input_filter.send_keys(id_siniestro)
        input_filter.send_keys(Keys.ENTER)
        input_filter.send_keys(Keys.ENTER)

        time.sleep(5)
        buttons = self.driver.find_elements(By.XPATH, "//button[@uib-tooltip='Ver']")
        button = buttons[0]

        for i in range(len(buttons)):
            button.click()
            time.sleep(5)
            self.driver.find_element(
                By.XPATH, "//button[@uib-tooltip='Cerrar']"
            ).click()
            time.sleep(5)
            if i < len(buttons) - 1:
                input_filter = self.driver.find_element(By.ID, "newdefaultfilter")
                input_filter.send_keys(id_siniestro)
                input_filter.send_keys(Keys.ENTER)
                input_filter.send_keys(Keys.ENTER)
                time.sleep(5)
                button = self.driver.find_elements(
                    By.XPATH, "//button[@uib-tooltip='Ver']"
                )[i + 1]

        self.driver.close()
        return []

    @override
    def add_eventos_to_siniestro(
        self, eventos: list[Evento], id_siniestro: int
    ) -> None:
        self.driver = webdriver.Chrome()

        login_follow_up(self.driver)

        time.sleep(2)

        input_filter = self.driver.find_element(By.ID, "newdefaultfilter")
        input_filter.send_keys(id_siniestro)
        input_filter.send_keys(Keys.ENTER)
        input_filter.send_keys(Keys.ENTER)

        time.sleep(2)
        self.driver.find_element(
            By.XPATH, "//a/uib-tab-heading/span[text()='Plan metodológico']"
        ).click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@uib-tooltip='Ver']").click()

        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[@uib-tooltip='Cerrar']").click()

        self.driver.close()
