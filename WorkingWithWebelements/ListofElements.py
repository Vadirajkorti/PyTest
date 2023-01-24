from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

class LisofItems():

    def test(self):

        service = Service(executable_path=r"C:\VAD\driver\chromedriver.exe")
        driver = webdriver.Chrome(service=service)

        driver.maximize_window()
        driver.get('https://courses.letskodeit.com/practice')

        driver.implicitly_wait(10)

        radio_buttons = driver.find_elements(By.XPATH, "//input[contains(@type ,'radio') and contains(@name,'cars')]")
        size = len(radio_buttons)
        print(size)

        for i in radio_buttons:
            radio_is_selected = i.is_selected()

            if not radio_is_selected:
                i.click()
                time.sleep(2)









run = LisofItems()
run.test()

