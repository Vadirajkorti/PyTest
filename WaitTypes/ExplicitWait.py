import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ExplicitWait():
    def test(self):
        service = Service(executable_path=r"C:\VAD\driver\chromedriver.exe")
        driver = webdriver.Chrome(service=service)

        driver.maximize_window()
        #driver.get('https://letskodeit.teachable.com/')

        driver.execute_script("window.location ='https://letskodeit.teachable.com/';")

        driver.find_element(By.XPATH, "//a[@href='/sign_in']").click()
        time.sleep(5)

        #driver.find_element(By.XPATH, "//a[@href='/sign_in']").send_keys("user")

        wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotVisibleException])
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/sign_in']")))
        element.click()


run = ExplicitWait()
run.test()