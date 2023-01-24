from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

from selenium.webdriver import ActionChains

class Drag_N_Drop():


    def test(self):

        service = Service(r"C:\VAD\driver\chromedriver.exe")
        driver = webdriver.Chrome(service=service)

        driver.maximize_window()
        driver.execute_script("window.location = 'https://jqueryui.com/droppable/' ;")
        '''
        wait = WebDriverWait(driver, 5 )
        element1 = wait.until(EC.element_to_be_clickable((driver.find_element(By.ID, "draggable"))))
        element2 = wait.until(EC.element_to_be_clickable((driver.find_element(By.ID, "droppable"))))
        
        '''

        driver.implicitly_wait(10)

        from_ele = driver.find_element(By.XPATH, "//div[@id = 'draggable']")
        drop_ele = driver.find_element(By.XPATH, "//div[@id = 'droppable']")


        action = ActionChains(driver)
        #action.drag_and_drop(from_ele, drop_ele).perform()
        action.click_and_hold(from_ele).move_to_element().release().perform()



run = Drag_N_Drop()
run.test()



