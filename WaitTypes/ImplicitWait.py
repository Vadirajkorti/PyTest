import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class ImplicitWait():
    def test(self):
        service = Service(executable_path=r"C:\VAD\driver\chromedriver.exe")
        driver = webdriver.Chrome(service=service)

        driver.maximize_window()
        driver.get('https://letskodeit.teachable.com/')

        driver.implicitly_wait(5)

        driver.find_element(By.XPATH, "//a[@href='/sign_in']").click()
        time.sleep(5)

        driver.find_element(By.XPATH, "//a[@href='/sign_in']").send_keys("user")


run = ImplicitWait()
run.test()