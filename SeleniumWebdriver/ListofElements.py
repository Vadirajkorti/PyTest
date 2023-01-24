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

        element_list_class = driver.find_elements(By.CLASS_NAME, "inputs")
        length_class_items = len(element_list_class)

        if element_list_class is not None:
            print("The size of class list " + str(length_class_items))

        element_list_tag = driver.find_elements(By.TAG_NAME, "a")
        length_tag_items = len(element_list_tag)

        if element_list_tag is not None:
            print("The size of tag list " + str(length_tag_items))


runtests = FindIdName()
runtests.test()


