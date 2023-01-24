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

        driver.get('https://google.com')
        print(driver.current_url)
        print(driver.title)
        driver.refresh()

        driver.back()
        print(driver.current_url)
        driver.get(driver.current_url)

        driver.forward()
        driver.page_source


        driver.quit()





run = BrowserInteactions()
run.test()

