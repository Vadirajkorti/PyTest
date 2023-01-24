from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self,driver):
        self.driver = driver

    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@value='Login']"


    def getEmailId(self):
        return self.driver.find_element(By.ID, self._email_field )

    def getpassword(self):
        return self.driver.find_element(By.ID, self._password_field)

    def getloginButton(self):
        return self.driver.find_element(By.XPATH,self._login_button)

    def enterUsername(self,email):
        self.getEmailId.send_keys(email)

    def enterPassword(self,password):
        self.getEmailId.send_keys(password)

    def clickLogin(self):
        self.getloginButton().click()

    def login(self,username,password):
        self.enterUsername()
        self.enterPassword()
        self.clickLogin()




