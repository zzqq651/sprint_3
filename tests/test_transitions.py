from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from sprint_3.locators import TestAllLocators


class TestTransitions:
    email = 'sokolov.daniil9@yandex.ru'
    password = 'qwerty123456'

    def test_switching_click_the_Constructor(self, driver):
        driver.find_element(*TestAllLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAllLocators.form_for_filling))
        driver.find_element(*TestAllLocators.field_registration_login).send_keys(TestTransitions.email)
        driver.find_element(*TestAllLocators.field_registration_password).send_keys(TestTransitions.password)
        driver.find_element(*TestAllLocators.button_input).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(TestAllLocators.button_personal_account))
        driver.find_element(*TestAllLocators.button_personal_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestAllLocators.button_exit))
        driver.find_element(*TestAllLocators. button_constructor).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestAllLocators.title_collect_burger))
        burger_link = driver.find_element(*TestAllLocators.title_collect_burger)
        assert burger_link.text == 'Соберите бургер'

    def test_switching_click_the_logo_Stellar_Burgers(self, driver):
        driver.find_element(*TestAllLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAllLocators.form_for_filling))
        driver.find_element(*TestAllLocators.field_registration_login).send_keys(TestTransitions.email)
        driver.find_element(*TestAllLocators.field_registration_password).send_keys(TestTransitions.password)
        driver.find_element(*TestAllLocators.button_input).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(TestAllLocators.button_personal_account))
        driver.find_element(*TestAllLocators.button_personal_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestAllLocators.button_exit))
        driver.find_element(*TestAllLocators.button_stellar_burgers).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(TestAllLocators.title_collect_burger))
        burger_link = driver.find_element(*TestAllLocators.title_collect_burger)
        assert burger_link.text == 'Соберите бургер'

    def test_check_history_orders(self, driver):
        driver.find_element(*TestAllLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestAllLocators.form_for_filling))
        driver.find_element(*TestAllLocators.field_registration_login).send_keys(TestTransitions.email)
        driver.find_element(*TestAllLocators.field_registration_password).send_keys(TestTransitions.password)
        driver.find_element(*TestAllLocators.button_input).click()
        WebDriverWait(driver, 8).until(
        expected_conditions.visibility_of_element_located(TestAllLocators.button_personal_account))
        driver.find_element(*TestAllLocators.button_personal_account).click()
        WebDriverWait(driver, 8).until(
        expected_conditions.visibility_of_element_located(TestAllLocators.button_history_shop))
        history_shop = driver.find_element(*TestAllLocators.button_history_shop)
        assert history_shop.text == 'История заказов'
