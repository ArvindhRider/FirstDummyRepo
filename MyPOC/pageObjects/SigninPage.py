from selenium.webdriver.common.by import By
from selenium import webdriver


class SigninPage:

    def __init__(self, driver):
        self.driver = driver

    emailTuple = (By.XPATH, "//input[@id='email']")
    pwdTuple = (By.XPATH, "//input[@id='passwd']")

    def email(self):
        return self.driver.find_element(*SigninPage.emailTuple)

    def pwd(self):
        return self.driver.find_element(*SigninPage.pwdTuple)
