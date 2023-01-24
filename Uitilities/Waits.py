import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Uitilities.wrappers import HandWrappers


class GenericWait():

    def __init__(self, driver):
        self.driver = driver
        self.hw = HandWrappers(driver)

    def wait(self, locator, locator_type, timeout=10, poll_freq=0.5):

        element = None
        try:
            wait = WebDriverWait(driver, timeout=10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotVisibleException])
            element = wait.until(EC.visibility_of_element_located((HandWrappers.getBytype(), locator)))
            element.click()
        except:
            print("Element not available")
        return element


