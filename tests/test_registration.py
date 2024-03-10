from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Sprint_5.tests.elements_to_find import TestLocators


class TestRegistration:

    def test_registration_success(self, driver):
        driver.find_element(*TestLocators.LOG_IN_BUTTON).click()
        driver.find_element(*TestLocators.REGISTRATION).click()
        driver.find_element(*TestLocators.NAME_REG).send_keys("Серафима")
        driver.find_element(*TestLocators.EMAIL).send_keys("serafima_timkova_6_289@yandex.com")
        driver.find_element(*TestLocators.PASSWORD).send_keys("tHisIS1")
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*TestLocators.EMAIL_2).send_keys("serafima_timkova_6_289@yandex.com")
        driver.find_element(*TestLocators.PASSWORD_2).send_keys("tHisIS1")
        driver.find_element(*TestLocators.LOG_IN_BUTTON_2).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.FORM_ORDER))
        assert driver.find_element(*TestLocators.FORM_ORDER).text == "Оформить заказ"

    def test_password_registration_error(self, driver):
        driver.find_element(*TestLocators.LOG_IN_BUTTON).click()
        driver.find_element(*TestLocators.REGISTRATION).click()
        driver.find_element(*TestLocators.NAME_REG).send_keys("Серафима")
        driver.find_element(*TestLocators.EMAIL).send_keys("serafima_timkova_6_790@yandex.com")
        driver.find_element(*TestLocators.PASSWORD).send_keys("123")
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        assert driver.find_element(*TestLocators.INCORRECT_PASS).text == "Некорректный пароль"
