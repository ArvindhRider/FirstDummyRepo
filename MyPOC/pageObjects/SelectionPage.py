from selenium.webdriver.common.by import By
from selenium import webdriver




class SelectionPage:
    def __init__(self, driver):
        self.driver = driver


    pdctTuple = (By.XPATH, "//li[@class='ajax_block_product col-xs-12 col-sm-6 col-md-4 first-in-line first-item-of-tablet-line first-item-of-mobile-line']/div/div[2]/div/a")
    chckoutTuple = (By.XPATH, "//a[@class='btn btn-default button button-medium']")


    def pdct(self):
        return self.driver.find_element(*SelectionPage.pdctTuple)

    def chck(self):
        return self.driver.find_element(*SelectionPage.chckoutTuple)


