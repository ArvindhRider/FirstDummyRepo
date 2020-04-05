from selenium.webdriver.common.by import By
from selenium import webdriver




class BillingPage:
    def __init__(self, driver):
        self.driver = driver

    billTuple =(By.XPATH, "//a[@class='button btn btn-default standard-checkout button-medium']")

    def bill(self):
        return self.driver.find_element(*BillingPage.billTuple)
