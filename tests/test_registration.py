from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from sprint_3.locators import TestAllLocators
import random


class TestRegistration:
    name = 'User'
    email = f"sokolov.daniil9{random.randint(100, 999)}@yandex.ru"
    password = f"{random.randint(100, 999)}+{random.randint(100, 999)}"

    def test_registration_input_a_password_of_3_symbols(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestAllLocators.field_registration_name).send_keys(TestRegistration.name)
        driver.find_element(*TestAllLocators.field_registration_login).send_keys(TestRegistration.email)
        password_locator = driver.find_element(*TestAllLocators.field_registration_password)
        password_locator.send_keys('123')
        assert len(password_locator.get_attribute('value')) <= 6

    def test_registration_input_a_password_of_3_symbols_and_check_issue(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAllLocators.form_for_filling))
        driver.find_element(*TestAllLocators.field_registration_name).send_keys(TestRegistration.name)
        driver.find_element(*TestAllLocators.field_registration_login).send_keys(TestRegistration.email)
        driver.find_element(*TestAllLocators.field_registration_password).send_keys('234')
        driver.find_element(*TestAllLocators.button_registration).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAllLocators.issue_for_incorrect_password))
        issue = driver.find_element(*TestAllLocators.issue_for_incorrect_password)
        assert issue.text == 'Некорректный пароль'

    def test_registration_filling_in_the_name_and_email_fields(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAllLocators.title_entry))
        field_registration_name = driver.find_element(*TestAllLocators.field_registration_name)
        field_registration_name.send_keys(TestRegistration.name)
        field_registration_login = driver.find_element(*TestAllLocators.field_registration_login)
        field_registration_login.send_keys(TestRegistration.email)
        filling_name = field_registration_name.get_attribute('value')
        filling_email = field_registration_login.get_attribute('value')
        assert filling_name == TestRegistration.name and filling_email == TestRegistration.email

    def test_registration_successful_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAllLocators.title_entry))
        driver.find_element(*TestAllLocators.field_registration_name).send_keys(TestRegistration.name)
        driver.find_element(*TestAllLocators.field_registration_login).send_keys(TestRegistration.email)
        driver.find_element(*TestAllLocators.field_registration_password).send_keys(TestRegistration.password)
        driver.find_element(*TestAllLocators.button_registration).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAllLocators.title_entry))
        assert 'Регистрация' in driver.find_element(*TestAllLocators.title_entry).text