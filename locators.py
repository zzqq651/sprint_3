from selenium.webdriver.common.by import By


class TestAllLocators:

    form_for_filling = By.CLASS_NAME, "Auth_login__3hAey"  # Форма для заполнения

    field_registration_name = By.XPATH, "//label[text()='Имя']/following-sibling::input"  # Поле Имя в форме регистрации

    field_registration_login = By.XPATH, "//label[text()='Email']/following-sibling::input"  # Поле email в форме регистрации

    field_registration_password = By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @type='password']"  # Поле пароля в форме регистрации

    button_registration = By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"  # Кнопка "Зарегистрироваться "

    issue_for_incorrect_password = By.XPATH, ".//p[@class='input__error text_type_main-default']"   # Ошибка для некорректного пароля

    field_email = By.XPATH, "//label[text()='Email']/following-sibling::input"  # Поле email на экране входа

    button_input = By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"  # Кнопка Войти

    button_input_registration = By.LINK_TEXT, 'Войти'  # Кнопка "Войти" на странице регистрации

    button_input_to_account = By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg' and text()='Войти в аккаунт']"  # Кнопка Войти в аккаунт

    return_password = By.XPATH, ".//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']"  # Кнопка Восстановить пароль

    button_input_return_password = By.XPATH, ".//a[@class='Auth_link__1fOlj' and text()='Войти']"  # Кнопка Войти на странице восстановить пароль

    button_personal_account = By.LINK_TEXT, 'Личный Кабинет'  # Кнопка Личный кабинет

    button_exit = By.XPATH, ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']"  # Кнопка Выход на странице Личного кабинета

    button_history_shop = (By.XPATH, ".//li[@class='Account_listItem__35dAP']/a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")  # Кнопка история заказов на странице Личного кабинета

    title_entry = By.XPATH, ".//div[@class='Auth_login__3hAey']/h2"  # Заголовок ВХОД

    button_constructor = By.LINK_TEXT, 'Конструктор'  # Кнопка Конструктор

    title_collect_burger = By.XPATH, ".//section[@class='BurgerIngredients_ingredients__1N8v2']/h1"  # Заголовок соберите бургер

    button_stellar_burgers = By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/a"  # Кнопка Stellar Burgers

    button_place_an_order = By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg' and text()='Оформить заказ']"  # Кнопка оформить заказ

    button_sauces = By.XPATH, ".//span[@class='text text_type_main-default' and text()='Соусы']"  # Кнопка Соусы

    title_sauce = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']" #Название Соусы

    example_sauce_spicy_x = By.XPATH, ".//p[@class='BurgerIngredient_ingredient__text__yp3dH' and text()='Соус Spicy-X']"  # Соус Spicy-X

    button_fillings = By.XPATH, ".//span[@class='text text_type_main-default' and text()='Начинки']"  # Кнопка Начинки

    title_fillings = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']"  # Название Начинки

    example_fillings_steak = By.XPATH, ".//p[@class='BurgerIngredient_ingredient__text__yp3dH' and text()='Говяжий метеорит (отбивная)']"  # Говяжий метеорит (отбивная)

    button_breads = By.XPATH, ".//span[@class='text text_type_main-default' and text()='Булки']"   # Кнопка Булки

    title_breads = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']"  # Название Булки

    example_breads_r2_d3 = By.XPATH, ".//p[@class='BurgerIngredient_ingredient__text__yp3dH' and text()='Флюоресцентная булка R2-D3']"  # Флюоресцентная булка R2-D3

