import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PageOjects.Pages.login_page import LoginPage

import unittest

class LoginTests(unittest.TestCase):

    def test_validLogin(self):

        service = Service(r"C:\VAD\driver\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.execute_script("window.location = 'https://courses.letskodeit.com/login' ;")

        lp = LoginPage(driver)
        lp.login('test@gmail.com','abcabc')

        userIcon  = driver.find_element(By.XPATH,"//span[text()='My Account']")

        if userIcon is not None:
            print("Login successful")

        else:
            print("Login not successful")

run = LoginTests()

run.test_validLogin()

