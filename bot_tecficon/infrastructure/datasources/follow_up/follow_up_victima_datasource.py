
from typing import override
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from ....config.constants import environment

from ....domain.entities import Victima
from ....domain.datasources import VictimasDatasource


class SinappSiniestrosDatasource(VictimasDatasource):
    def __init__(self):
        self.driver: webdriver.Chrome

    def login(self) -> None:
        self.driver.get(environment.BASE_URL_FOLLOW_UP)

        self.driver.find_element(By.NAME, "user").send_keys(
            environment.USER_FOLLOW_UP)
        self.driver.find_element(By.NAME, "password").send_keys(
            environment.PASS_FOLLOW_UP)
        self.driver.find_element(By.CSS_SELECTOR, ".ladda-button").click()

        time.sleep(5)

        self.driver.find_element(
            By.CSS_SELECTOR, "#callProductsButton > .ng-binding").click()
        self.driver.find_element(
            By.CSS_SELECTOR, ".ng-scope:nth-child(1) > .ng-binding > .bluelight-color").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-info").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".fa-file").click()

    @override
    def get_victimas_by_siniestro(self, id_siniestro: str) -> list[Victima]:
        raise

    @override
    def add_victima_to_siniestro(self, victima: Victima, id_siniestro: str) -> bool:
        self.driver = webdriver.Chrome()

        self.login()

        time.sleep(5)

        self.driver.find_element(By.ID, "newclaimid").send_keys(id_siniestro)
        self.driver.find_element(
            By.ID, "newclaimpatientdocument").send_keys()  # ?
        self.driver.find_element(By.ID, "").send_keys()

        return True
