
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

        self.driver.get(environment.BASE_URL_ALLIA2)
        self.driver.set_window_size(968, 612)
        self.driver.find_element(By.ID, "nx-input-0").send_keys(environment.USER_ALLIA2)
        self.driver.find_element(By.ID, "nx-input-1").click()
        self.driver.find_element(By.ID, "nx-input-1").send_keys(environment.PASS_ALLIA2)
        self.driver.find_element(By.CSS_SELECTOR, ".nx-button__content-wrapper").click()
        time.sleep(5)
        element = self.driver.find_element(By.CSS_SELECTOR, ".c-main-navbar__link")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        time.sleep(2)
        subnavbar_el = self.driver.find_element(By.CSS_SELECTOR, ".c-subnavbar__item:nth-child(2) .c-subnavbar__title")
        actions.move_to_element(subnavbar_el).click().perform()
        time.sleep(2)
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.ID, "PENDING").click()
        try:
            self.driver.find_element(By.XPATH, f"//*[contains(text(), '{siniestro_id}')]").click()
        except:
            self.driver.quit()
            raise SiniestroNoExisteError(siniestro_id)

        time.sleep(5)
        self.driver.quit()

        raise

    @override
    def add_siniestro(self, siniestro: Siniestro) -> bool:
        raise
