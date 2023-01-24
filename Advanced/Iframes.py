import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


class Iframe():

    def test(self):
        service = Service(r"C:\VAD\driver\chromedriver.exe")
        driver = webdriver.Chrome(service=service)

        driver.maximize_window()
        driver.execute_script("window.location = 'https://courses.letskodeit.com/practice/' ;")
        file_name = r"C:\VAD\Pytest\Advanced\test.png"

        driver.execute_script("window.scrollBy(0,500);")
        driver.save_screenshot(file_name)



        #using id
        driver.switch_to.frame("courses-iframe")

        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable(driver.find_element(By.ID, "search")))


        search = driver.find_element(By.ID, "search")
        search.send_keys("Python")
        time.sleep(2)

        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0,-500);")

        driver.find_element(By.ID,'name').send_keys("Test Successful")


run = Iframe()
run.test()