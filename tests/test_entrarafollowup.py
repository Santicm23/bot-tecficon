# Generated by Selenium IDE
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestEntrarafollowup():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_entrarafollowup(self):
        self.driver.get("https://sec-co.controlexpert.com/platform/")

        self.driver.find_element(By.NAME, "user").send_keys("hurtado.gandini")
        self.driver.find_element(By.NAME, "password").send_keys("Allianz2023*")
        self.driver.find_element(By.CSS_SELECTOR, ".ladda-button").click()
        time.sleep(5)
        self.driver.find_element(
            By.CSS_SELECTOR, "#callProductsButton > .ng-binding").click()
        self.driver.find_element(
            By.CSS_SELECTOR, ".ng-scope:nth-child(1) > .ng-binding > .bluelight-color").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-info").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".fa-file").click()
        time.sleep(5)
        
