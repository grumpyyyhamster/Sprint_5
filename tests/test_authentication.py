from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Sprint_5.tests.elements_to_find import TestLocators
from tests.data_to_use import TestData


class TestAuthentication:
    def test_log_in_main_success(self, driver):
        driver.find_element(*TestLocators.LOG_IN_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_2).send_keys(TestData.EMAIL)
        driver.find_element(*TestLocators.PASSWORD_2).send_keys(TestData.PASS)
        driver.find_element(*TestLocators.LOG_IN_BUTTON_2).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.FORM_ORDER))
        assert driver.find_element(*TestLocators.FORM_ORDER).text == "Оформить заказ"

    def test_log_in_personal_info_success(self, driver):
        driver.find_element(*TestLocators.PERSONAL_INFO).click()
        driver.find_element(*TestLocators.EMAIL_2).send_keys(TestData.EMAIL)
        driver.find_element(*TestLocators.PASSWORD_2).send_keys(TestData.PASS)
        driver.find_element(*TestLocators.LOG_IN_BUTTON_2).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.FORM_ORDER))
        assert driver.find_element(*TestLocators.FORM_ORDER).text == "Оформить заказ"

    def test_log_in_registration_form_success(self, driver):
        driver.get(TestData.REG_PAGE)
        driver.find_element(*TestLocators.LOG_IN_BUTTON_3).click()
        driver.find_element(*TestLocators.EMAIL_2).send_keys(TestData.EMAIL)
        driver.find_element(*TestLocators.PASSWORD_2).send_keys(TestData.PASS)
        driver.find_element(*TestLocators.LOG_IN_BUTTON_2).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.FORM_ORDER))
        assert driver.find_element(*TestLocators.FORM_ORDER).text == "Оформить заказ"

    def test_log_in_forgot_pass_success(self, driver):
        driver.get(TestData.LOG_IN_PAGE)
        driver.find_element(*TestLocators.FORGOT_PASS).click()
        driver.find_element(*TestLocators.LOG_IN_BUTTON_3).click()
        driver.find_element(*TestLocators.EMAIL_2).send_keys(TestData.EMAIL)
        driver.find_element(*TestLocators.PASSWORD_2).send_keys(TestData.PASS)
        driver.find_element(*TestLocators.LOG_IN_BUTTON_2).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.FORM_ORDER))
        assert driver.find_element(*TestLocators.FORM_ORDER).text == "Оформить заказ"
