from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

class BrowserInteactions():

    def test(self):

        service = Service(executable_path=r"C:\VAD\driver\chromedriver.exe")
        driver = webdriver.Chrome(service=service)

        driver.maximize_window()
        driver.get('https://letskodeit.teachable.com/')
        print(driver.title)


        _course = "//div[@class='container']//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
        _course_locator = _course.format('Selenium WebDriver With Python 3.x')

        element = driver.find_element(By.XPATH,_course_locator)
        element.click()

        time.sleep(5)



        driver.quit()





run = BrowserInteactions()
run.test()

