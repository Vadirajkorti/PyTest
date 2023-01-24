from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

class SwitchWindow():

    def test(self):

        service = Service(r"C:\VAD\driver\chromedriver.exe")
        driver = webdriver.Chrome(service=service)

        driver.maximize_window()
        driver.execute_script("window.location = 'https://courses.letskodeit.com/practice/' ;")
        file_name = r"C:\VAD\Pytest\Advanced\test.png"


        driver.execute_script("window.scrollBy(0,100);")
        driver.save_screenshot(file_name)

        height = driver.execute_script("return window.innerHeight ;")
        width = driver.execute_script("return window.innerWidth ;")

        print("Height", height, "\n Width", width)

        current_win = driver.current_window_handle
        print(current_win)

        driver.find_element(By.XPATH, "//button[@id='openwindow']").click()

        


        all_windows = driver.window_handles
        print(all_windows)

        for i in all_windows:
            if i == 'CDwindow-FD46FBB8DAA4C54BCF20B01249744865':
                driver.switch_to(i)
                break

        print(driver.title)














run = SwitchWindow()
run.test()
