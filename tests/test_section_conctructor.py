from sprint_3.locators import TestAllLocators


class TestSectionConstructor:

    def test_constructor_switch_to_sauces(self, driver):
        driver.find_element(*TestAllLocators.button_sauces).click()
        title_sauce = driver.find_element(*TestAllLocators.title_sauce)
        example_sauce = driver.find_element(*TestAllLocators.example_sauce_spicy_x)
        assert title_sauce.text == 'Соусы' and example_sauce.text == 'Соус Spicy-X'

    def test_constructor_switch_to_fillings(self, driver):
        driver.find_element(*TestAllLocators.button_fillings).click()
        title_fillings = driver.find_element(*TestAllLocators.title_fillings)
        example_fillings = driver.find_element(*TestAllLocators.example_fillings_steak)
        assert title_fillings.text == 'Начинки' and example_fillings.text == 'Говяжий метеорит (отбивная)'

    def test_constructor_switch_to_breads(self, driver):
        driver.find_element(*TestAllLocators.button_fillings).click()
        driver.find_element(*TestAllLocators.button_breads).click()
        title_breads = driver.find_element(*TestAllLocators.title_breads)
        example_breads = driver.find_element(*TestAllLocators.example_breads_r2_d3)
        assert title_breads.text == 'Булки' and example_breads.text == 'Флюоресцентная булка R2-D3'