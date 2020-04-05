import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# @pytest.mark.usefixtures("setup")
# from pageObjects.SelectionPage import SelectionPage
from pageObjects.BillingPage import BillingPage
from pageObjects.SigninPage import SigninPage
from pageObjects.homePage import homePage
from utilities.BaseClass import BaseClass


# from pageObjects.BillingPage import BillingPage


class TestOne(BaseClass):
    def test_poc(self):
        log = self.getLogger()      # using self logger form base class to get the logs
        hp = homePage(self.driver)
        bip = BillingPage(self.driver)
        sgp = SigninPage(self.driver)
        # sp = SelectionPage(self.driver) // page object mechanism

        # driver.maximize_window()

        # Homepage login basics
        # HomePageChecker = self.driver.find_element_by_xpath("//a[@class='homefeatured']").text   // page objected in homePage
        HomePageChecker = hp.validation().text
        print(HomePageChecker)
        if HomePageChecker == "POPULAR":
            print("HomePage Validation successful")
        # self.driver.find_element_by_xpath("//input[@id='search_query_top']").click()   // page objected in homePage
        hp.search().click()
        # self.driver.find_element_by_xpath("//input[@id='search_query_top']").send_keys("printed")     //  page objected in homePage
        #hp.search().send_keys("printed")
        hp.search().send_keys("printed")
        # self.driver.find_element_by_css_selector(".button-search").click()  //page objected in homePage
        # hp.button().click  //page object mechanism
        sp = hp.button()  # minimizing page object mechanism here with adding the sp object inside homepage itself and using sp as an variable

        # time.sleep(5) # use explicit wait here
        wait = WebDriverWait(self.driver, 4)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                    "//li[@class='ajax_block_product col-xs-12 col-sm-6 col-md-4 first-in-line first-item-of-tablet-line first-item-of-mobile-line']/div/div[2]/div/a")))

        # product = self.driver.find_element_by_xpath(
        # "//li[@class='ajax_block_product col-xs-12 col-sm-6 col-md-4 first-in-line first-item-of-tablet-line first-item-of-mobile-line']/div/div[2]/div/a")
        product = sp.pdct()
        product.click()

        # wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[@class='btn btn-default button button-medium']")))
        # wait.until(expected_conditions.invisibility_of_element_located)

        time.sleep(5)
        # checkout = self.driver.find_element_by_xpath("//a[@class='btn btn-default button button-medium']")
        checkout = sp.chck()
        checkout.click()


        # Checkout page validation
        reConfirmation = self.driver.find_element_by_xpath(
            "//td[@class='cart_description']//a[contains(text(),'Printed Summer Dress')]").text
        print(reConfirmation)
        assert reConfirmation == 'Printed Summer Dress'

        # CheckoutPage to nter the emailand passweod
        #

        #self.driver.find_element_by_xpath(
        #"//a[@class='button btn btn-default standard-checkout button-medium']").click()
        bip.bill().click()
        log.info("Entering email address")
        sgp.email().send_keys("abra@dummy.com")
        log.info("Entering password")
        sgp.pwd().send_keys("abra")




        # email - //input[@id='email']
        # pwd - //input[@id='passwd']
        # sigin - //button[@id='SubmitLogin']
