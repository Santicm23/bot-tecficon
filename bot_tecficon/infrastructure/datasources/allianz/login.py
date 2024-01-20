
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


from ....config.constants import environment
from ....domain.errors import InicioSesionError


def login_allianz(driver: webdriver.Chrome) -> None:
    try:
        # Login
        driver.get(environment.BASE_URL_ALLIANZ)
        # driver.set_window_size(width=968, height=612)
        driver.find_element(
            By.ID, "nx-input-0").send_keys(environment.USER_ALLIANZ)
        driver.find_element(By.ID, "nx-input-1").click()
        driver.find_element(
            By.ID, "nx-input-1").send_keys(environment.PASS_ALLIANZ)
        driver.find_element(
            By.CSS_SELECTOR, ".nx-button__content-wrapper").click()
        time.sleep(5)

        # Entrar a página de siniestros
        element = driver.find_element(
            By.CSS_SELECTOR, ".c-main-navbar__link")
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
        time.sleep(2)
        subnavbar_el = driver.find_element(
            By.CSS_SELECTOR, ".c-subnavbar__item:nth-child(2) .c-subnavbar__title")
        actions.move_to_element(subnavbar_el).click().perform()
        time.sleep(3)
        driver.switch_to.frame(0)
        driver.find_element(By.ID, "PENDING").click()
    except Exception:
        raise InicioSesionError('Allianz')
