import random

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Sprint_5.tests.elements_to_find import TestLocators
from tests.data_to_use import TestData


class TestRegistration:

    def test_registration_success(self, driver):
        random_email = f"serafima_timkova_6_{random.randint(100, 999)}@yandex.com"
        driver.find_element(*TestLocators.LOG_IN_BUTTON).click()
        driver.find_element(*TestLocators.REGISTRATION).click()
        driver.find_element(*TestLocators.NAME_REG).send_keys(TestData.REG_NAME)
        driver.find_element(*TestLocators.EMAIL).send_keys(random_email)
        driver.find_element(*TestLocators.PASSWORD).send_keys(TestData.REG_PASS)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        driver.get(TestData.LOG_IN_PAGE)
        driver.find_element(*TestLocators.EMAIL_2).send_keys(random_email)
        driver.find_element(*TestLocators.PASSWORD_2).send_keys(TestData.REG_PASS)
        driver.find_element(*TestLocators.LOG_IN_BUTTON_2).click()
        WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located(TestLocators.FORM_ORDER))
        assert driver.find_element(*TestLocators.FORM_ORDER).text == "Оформить заказ"

    def test_password_registration_error(self, driver):
        driver.find_element(*TestLocators.LOG_IN_BUTTON).click()
        driver.find_element(*TestLocators.REGISTRATION).click()
        driver.find_element(*TestLocators.NAME_REG).send_keys(TestData.REG_NAME)
        driver.find_element(*TestLocators.EMAIL).send_keys(TestData.RANDOM_EMAIL)
        driver.find_element(*TestLocators.PASSWORD).send_keys(TestData.INCORRECT_PASS)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        assert driver.find_element(*TestLocators.INCORRECT_PASS).text == "Некорректный пароль"
