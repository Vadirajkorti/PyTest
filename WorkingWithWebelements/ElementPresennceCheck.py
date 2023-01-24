from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Uitilities import wrappers

import time

class Dropdowns():

    def test(self):

        service = Service(executable_path=r"C:\VAD\driver\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        driver.get('https://courses.letskodeit.com/practice')

        hw =wrappers.HandWrappers(driver)

        ele_pres = hw.isElementPresent('name', By.ID)
        print(str(ele_pres))

        ele_pres2 = hw.checkElementPresence("//input[@id,'name']", By.XPATH)
        print(str(ele_pres2))





run = Dropdowns()
run.test()

