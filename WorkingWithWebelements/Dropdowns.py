from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time

class Dropdowns():

    def test(self):

        service = Service(executable_path=r"C:\VAD\driver\chromedriver.exe")
        driver = webdriver.Chrome(service=service)

        driver.maximize_window()

        driver.get('https://courses.letskodeit.com/practice')

        driver.implicitly_wait(10)

        element = driver.find_element(By.ID, "carselect")
        sel = Select(element)

        sel.select_by_index("2")
        time.sleep(2)
        sel.select_by_value("benz")
        time.sleep(2)
        sel.select_by_visible_text("BMW")
        time.sleep(2)

        driver.get("https://www.expedia.co.in/?pwaLob=wizard-car-pwa")

        ele = driver.find_element(By.XPATH, "//select[@aria-label='Pick-up time']")
        sel = Select(ele)

        sel.select_by_value('00:15')
        time.sleep(2)





















run = Dropdowns()
run.test()

