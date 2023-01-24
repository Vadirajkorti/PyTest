from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service

from selenium.webdriver.common.by import By


class RunChromeTests():

    def test(self):

        service = Service(executable_path="C:\\VAD\\driver\\chromedriver.exe")
        #Instanciate Service
        driver = webdriver.Chrome(service=service)
        #Open Url
        driver.get("https://google.com")
        #driver.find_element(By.Xpath , //div[@class='FPdoLc lJ9FBc']//input[@class='gNO89b'])

chrome =RunChromeTests()
chrome.test()