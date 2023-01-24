from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class FindXpathCSS():
    def test(self):
        service = Service(executable_path=r"C:\VAD\driver\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        baseUrl = "https://courses.letskodeit.com/practice"
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        elementbyXpath = driver.find_element(By.XPATH, '//input[@id="displayed-text"]')

        if elementbyXpath is not None:
            print("Element Found by -> Xpath")

        elementByCSS = driver.find_element(By.CSS_SELECTOR, "#show-textbox")

        if elementByCSS is not None:
            print("Element Found by -> CSS")


runtests = FindXpathCSS()
runtests.test()




