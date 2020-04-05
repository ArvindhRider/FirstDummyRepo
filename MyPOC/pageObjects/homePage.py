from selenium.webdriver.common.by import By
from selenium import webdriver

from pageObjects.SelectionPage import SelectionPage


class homePage:

    def __init__(self, driver):
        self.driver = driver

    hpvalidationTuple = (By.XPATH, "//a[@class='homefeatured']")
    searchTuple = (By.XPATH, "//input[@id='search_query_top']")
    buttonTuple = (By.CSS_SELECTOR, ".button-search")


    def search(self):
        return self.driver.find_element(*homePage.searchTuple)

    def button(self):
        #return self.driver.find_element(*homePage.buttonTuple)
        self.driver.find_element(*homePage.buttonTuple).click()
        sp = SelectionPage(self.driver)
        return sp



    def validation(self):
        return self.driver.find_element(*homePage.hpvalidationTuple)

