import time
from typing import override

from selenium import webdriver
from selenium.webdriver.common.by import By

from ....domain.datasources import VictimasDatasource
from ....domain.entities import Victima
from .login import login_follow_up


class FollowUpVictimasDatasource(VictimasDatasource):
    def __init__(self):
        self.driver: webdriver.Chrome

    @override
    def get_victimas_by_siniestro(self, id_siniestro: str) -> list[Victima]:
        raise

    @override
    def add_victima_to_siniestro(self, victima: Victima, id_siniestro: str) -> None:
        self.driver = webdriver.Chrome()

        login_follow_up(self.driver)

        time.sleep(5)

        self.driver.find_element(By.ID, "newclaimid").send_keys(id_siniestro)
        self.driver.find_element(By.ID, "newclaimpatientdocument").send_keys()  # ?
        self.driver.find_element(By.ID, "").send_keys()

        raise
