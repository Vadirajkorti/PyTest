from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumDriver():

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


    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            self.driver.implicitly_wait(0)
            byType = self.hw.getByType(locatorType)
            print("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((byType, locator)))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        self.driver.implicitly_wait(2)
        return element
