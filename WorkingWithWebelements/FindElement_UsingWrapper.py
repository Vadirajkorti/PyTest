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
        driver.get("https://www.expedia.co.in/?pwaLob=wizard-car-pwa")

        hw =wrappers.HandWrappers(driver)

        ele = hw.getElement("xpath", "//select[@aria-label='Pick-up time']")
        sel = Select(ele)

        sel.select_by_value('00:15')
        time.sleep(2)


run = Dropdowns()
run.test()

