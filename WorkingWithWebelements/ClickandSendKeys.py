from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

class BrowserInteactions():

    def test(self):

        service = Service(executable_path=r"C:\VAD\driver\chromedriver.exe")
        driver = webdriver.Chrome(service=service)

        driver.maximize_window()
        driver.get('https://courses.letskodeit.com/practice')
        print(driver.title)

        loginLink= driver.find_element(By.XPATH,'//div[contains(@class,"collapse navbar-collapse")]//a[@href="/login"]')
        loginLink.click()

        email_field = driver.find_element(By.ID, 'email')
        email_field.send_keys('test')

        password_field = driver.find_element(By.ID, 'password')
        password_field.send_keys('test')

        time.sleep(3)
        email_field.clear()


        time.sleep(3)
        email_field.send_keys('test')


        driver.quit()





run = BrowserInteactions()
run.test()

