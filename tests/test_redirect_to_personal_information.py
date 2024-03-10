from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Sprint_5.tests.elements_to_find import TestLocators


class TestRedirectPersonalInfo:
    def test_redirect_to_personal_info_success(self, driver):
        driver.find_element(*TestLocators.LOG_IN_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_2).send_keys("serafima_timkova_6_123@yandex.com")
        driver.find_element(*TestLocators.PASSWORD_2).send_keys("tHisIS")
        driver.find_element(*TestLocators.LOG_IN_BUTTON_2).click()
        driver.find_element(*TestLocators.PERSONAL_INFO).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.CHANGE_INFO))
        assert driver.find_element(
            *TestLocators.CHANGE_INFO).text == "В этом разделе вы можете изменить свои персональные данные"
