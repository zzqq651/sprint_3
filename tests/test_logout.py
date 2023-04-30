from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from sprint_3.locators import TestAllLocators


class TestLogout:

    def test_log_out_log_out_from_account(self, driver):
        driver.find_element(*TestAllLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAllLocators.form_for_filling))
        driver.find_element(*TestAllLocators.field_registration_login).send_keys('sokolov.daniil9@yandex.ru')
        driver.find_element(*TestAllLocators.field_registration_password).send_keys('qwerty123456')
        driver.find_element(*TestAllLocators.button_input).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(TestAllLocators.button_personal_account))
        driver.find_element(*TestAllLocators.button_personal_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestAllLocators.button_exit))
        driver.find_element(*TestAllLocators.button_exit).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestAllLocators.title_entry))
        button = driver.find_element(*TestAllLocators.title_entry).text
        assert button == 'Вход'