from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from sprint_3.locators import TestAllLocators


class TestLogin:

    def test_login_in_the_registration_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAllLocators.form_for_filling))
        driver.find_element(*TestAllLocators.button_input_registration).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAllLocators.form_for_filling))
        driver.find_element(*TestAllLocators.field_registration_login).send_keys('sokolov.daniil9@yandex.ru')
        driver.find_element(*TestAllLocators.field_registration_password).send_keys('qwerty123456')
        driver.find_element(*TestAllLocators.button_input).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAllLocators.button_place_an_order))
        order_button = driver.find_element(*TestAllLocators.button_place_an_order)
        assert order_button.text == 'Оформить заказ'

    def test_login_personal_account(self, driver):
        driver.find_element(*TestAllLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAllLocators.form_for_filling))
        driver.find_element(*TestAllLocators.field_registration_login).send_keys('sokolov.daniil9@yandex.ru')
        driver.find_element(*TestAllLocators.field_registration_password).send_keys('qwerty123456')
        driver.find_element(*TestAllLocators.button_input).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAllLocators.button_place_an_order))
        order_button = driver.find_element(*TestAllLocators.button_place_an_order)
        assert order_button.text == 'Оформить заказ'

    def test_login_button_input_to_account(self, driver):
        driver.find_element(*TestAllLocators.button_input_to_account).click()
        driver.find_element(*TestAllLocators.field_registration_login).send_keys('sokolov.daniil9@yandex.ru')
        driver.find_element(*TestAllLocators.field_registration_password).send_keys('qwerty123456')
        driver.find_element(*TestAllLocators.button_input).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAllLocators.button_place_an_order))
        order_button = driver.find_element(*TestAllLocators.button_place_an_order)
        assert order_button.text == 'Оформить заказ'

    def test_login_password_recovery(self, driver):
        driver.find_element(*TestAllLocators.button_input_to_account).click()
        driver.find_element(*TestAllLocators.return_password).click()
        driver.find_element(*TestAllLocators.button_input_return_password).click()
        driver.find_element(*TestAllLocators.field_registration_login).send_keys('sokolov.daniil9@yandex.ru')
        driver.find_element(*TestAllLocators.field_registration_password).send_keys('qwerty123456')
        driver.find_element(*TestAllLocators.button_input).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAllLocators.button_place_an_order))
        order_button = driver.find_element(*TestAllLocators.button_place_an_order)
        assert order_button.text == 'Оформить заказ'
