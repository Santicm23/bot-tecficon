import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from ....config.constants import environment
from ....domain.errors import InicioSesionError


def login_follow_up(driver: webdriver.Chrome) -> None:
    try:
        driver.get(environment.BASE_URL_FOLLOW_UP)

        driver.find_element(By.NAME, "user").send_keys(environment.USER_FOLLOW_UP)
        driver.find_element(By.NAME, "password").send_keys(environment.PASS_FOLLOW_UP)
        driver.find_element(By.CSS_SELECTOR, ".ladda-button").click()

        time.sleep(2)

        driver.find_element(
            By.CSS_SELECTOR, "#callProductsButton > .ng-binding"
        ).click()
        driver.find_element(
            By.CSS_SELECTOR, ".ng-scope:nth-child(1) > .ng-binding > .bluelight-color"
        ).click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".btn-info").click()
        # driver.find_element(By.CSS_SELECTOR, ".fa-file").click()
        time.sleep(2)
    except Exception:
        raise InicioSesionError("Follow Up")


def go_back_follow_up() -> None:
    ...
