from selenium import webdriver
from selenium.webdriver.common.by import By


class HandWrappers():

    def __init__(self, driver):
        self.driver = driver

    def getBytype(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "tag":
            return By.TAG_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "partialLink":
            return By.PARTIAL_LINK_TEXT
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "class":
            return By.CLASS_NAME

        else:
            print("ELement not found")
        return False


    def getElement(self,locatorType, locator):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getBytype(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element Found")
        except:
            print("Element not found")

        return element

    def isElementPresent(self, locator, byType):
        element = None
        try:
            element = self.driver.find_element(byType, locator)
            if element is not None:
                print("Element Found")
                return True
            else:return False

        except:
            print("Element not found")
            return False

    def checkElementPresence(self,locator , byType):
        element  = None
        try:
            elements = self.driver.find_elements(byType,locator)
            if len(elements)>0:
                print("Element Found")
                return True
            else:
                return False

        except:
            print("Element not found")
            return False
