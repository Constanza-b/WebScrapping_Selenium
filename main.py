from selenium.webdriver import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait



USER = "standard_user"
PASSWORD = "secret_sauce"

def main():
    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    
    #option.add_argument("--headless")
    option.add_argument("--window-size=1920,1080")
    driver = Chrome(service=service, options=option)
    driver.get("https://www.saucedemo.com/")
    
    time.sleep(2)
    
    #LOGIN
    driver.find_element(By.ID, "user-name").send_keys(USER)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    
    #COMPRAS
    driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
    
    time.sleep(2)
    
    #CARRITO
    driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a/span").click()
    driver.find_element(By.ID, "checkout").click()
    time.sleep(2)
    
    FIRST_NAME = "Cony"
    LAST_NAME = "Becerra"
    CODE_POSTAL = "12345"
    
    
    #PAGAR
    driver.find_element(By.ID, "first-name").send_keys(FIRST_NAME)
    driver.find_element(By.ID, "last-name").send_keys(LAST_NAME)
    driver.find_element(By.ID, "postal-code").send_keys(CODE_POSTAL)
    time.sleep(2)
    
    driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[2]/input").click()
    time.sleep(2)
    
    driver.find_element(By.ID, "finish").click()
    
    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    main()