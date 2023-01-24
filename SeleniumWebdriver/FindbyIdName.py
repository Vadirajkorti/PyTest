from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.firefox.service import Service


class FindIdName():
    def test(self):
        service = Service(executable_path=r"C:\VAD\driver\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        baseUrl = "https://courses.letskodeit.com/practice"
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        elementbyId = driver.find_element(By.ID, "displayed-text")

        if elementbyId is not None:
            print("Element Found by -> Id")

        elementByName = driver.find_element(By.NAME, "show-hide")

        if elementByName is not None:
            print("Element Found by -> Name")


runtests = FindIdName()
runtests.test()

'''
class FindIdName_Gecko():
    def test(self):
        service = Service(executable_path=r"C:\VAD\driver\geckodriver.exe")
        driver = webdriver.Firefox(service=service)
        baseUrl="https://courses.letskodeit.com/practice"
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        elementbyId =driver.find_element(By.ID, "displayed-text")

        if elementbyId is not None:
            print("Element Found by -> Id")

        elementByName = driver.find_element(By.NAME,"show-hide")

        if elementByName is not None:
            print("Element Found by -> Name")

runtests_gecko = FindIdName_Gecko()
runtests_gecko.test()

'''
