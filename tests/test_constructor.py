from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Sprint_5.tests.elements_to_find import TestLocators


class TestConstructor:
    def test_redirect_to_buns_correct(self, driver):
        driver.find_element(*TestLocators.FILLINGS).click()
        driver.find_element(*TestLocators.BUNS).click()
        assert driver.find_element(*TestLocators.BUNS_TEXT).is_displayed()

    def test_redirect_to_sauces_correct(self, driver):
        driver.find_element(*TestLocators.SAUCES).click()
        assert driver.find_element(*TestLocators.SAUCES_TEXT).is_displayed()

    def test_redirect_to_fillings_correct(self, driver):
        driver.find_element(*TestLocators.FILLINGS).click()
        assert driver.find_element(*TestLocators.FILLINGS_TEXT).is_displayed()
