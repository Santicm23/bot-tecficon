
from selenium import webdriver
from selenium.webdriver.common.by import By


def iniciar_sesion() -> None:
    driver = webdriver.Chrome()

    driver.get("https://www.allia2net.com.co/ngx-epac-professional/public/home")
    driver.set_window_size(968, 612)
    driver.find_element(By.ID, "nx-input-0").send_keys("CP301484")
    driver.find_element(By.ID, "nx-input-1").click()
    driver.find_element(By.ID, "nx-input-1").send_keys("Hgdsas9012023")
    driver.find_element(By.CSS_SELECTOR, ".nx-icon--password-show-o").click()
    driver.find_element(By.CSS_SELECTOR, ".nx-button__content-wrapper").click()
    
    driver.quit()
