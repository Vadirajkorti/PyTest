from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

from selenium.webdriver import ActionChains

class SwitchWindow():

    def test(self):

        service = Service(r"C:\VAD\driver\chromedriver.exe")
        driver = webdriver.Chrome(service=service)

        driver.maximize_window()
        driver.execute_script("window.location = 'https://courses.letskodeit.com/practice/' ;")

        hovwer = driver.find_element(By.ID, 'mousehover')
        itemtoclick = "//a[normalize-space()='Top']"

        action = ActionChains(driver)
        action.move_to_element(hovwer).perform()

        top = driver.find_element(By.XPATH, itemtoclick)
        action.move_to_element(top).click().perform()


run = SwitchWindow()
run.test()



