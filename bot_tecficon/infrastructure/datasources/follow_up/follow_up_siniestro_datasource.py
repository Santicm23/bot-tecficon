
from typing import override
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from bot_tecficon.config.constants import environment

from ....domain.entities import Siniestro
from ....domain.datasources import SiniestrosDatasource


class SinappSiniestrosDatasource(SiniestrosDatasource):
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
    def get_all_siniestros(self) -> list[Siniestro]:
        raise

    @override
    def get_siniestro_by_id(self, id_siniestro: int) -> Siniestro:
        raise

    @override
    def add_siniestro(self, siniestro: Siniestro) -> None:
        self.driver = webdriver.Chrome()

        self.login()

        time.sleep(5)

        self.driver.find_element(By.ID, "newclaimid").send_keys(siniestro.numero_siniestro)
        self.driver.find_element(By.ID, "newclaimpatientdocument").send_keys() # ?
        self.driver.find_element(By.ID, "").send_keys()

