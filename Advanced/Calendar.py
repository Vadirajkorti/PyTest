import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

class Calendar_Check():

    def test(self):

        service = Service(executable_path=r"C:\VAD\driver\chromedriver.exe")
        driver = webdriver.Chrome(service=service)


        #wait = WebDriverWait(driver,5)
        #element = wait.until(Ec.element_to_be_clickable((By.XPATH,)))

        #dropdown = Select(ele)
        #dropdown.select_by_value("2")

        driver.maximize_window()

        baseUrl = "https://www.expedia.co.in/"
        driver.get(baseUrl)

        driver.find_element(By.XPATH, "//span[normalize-space()='Flights']").click()
        driver.find_element(By.CSS_SELECTOR, "button#d1-btn").click()
        dates = driver.find_elements(By.XPATH,"//div[@class='uitk-calendar']//div[1]//table[1]//tr//td//button[@class='uitk-date-picker-day']")
        time.sleep(5)
        for i in dates:
            print(i.get_attribute("aria-label"))
            if i.get_attribute("aria-label") =='22 Jan 2023':
                i.click()
                time.sleep(5)
                break


c=Calendar_Check()
c.test()



