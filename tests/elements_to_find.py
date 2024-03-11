from selenium.webdriver.common.by import By


class TestLocators:
    LOG_IN_BUTTON = By.XPATH, ".//section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']/div/button"  # Кнопка Войти в аккаунт на главной странице
    REGISTRATION = By.XPATH, ".//a[@href='/register']"  # Кнопка Зарегистрироваться на странице входа
    NAME_REG = By.XPATH, ".//label[text()='Имя']/following::input"  # Строка ввода Имени при регистрации пользователя
    EMAIL = By.XPATH, ".//label[text()='Email']/following::input"  # Строка ввода Имейла при регистрации пользователя
    EMAIL_2 = By.XPATH, ".//label[text()='Email']/following::input"  # Строка ввода Имейла при входе
    PASSWORD = By.XPATH, ".//label[text()='Пароль']/following::input"  # Строка ввода Пароля при регистрации пользователя
    PASSWORD_2 = By.XPATH, ".//label[text()='Пароль']/following::input"  # Строка ввода Пароля при входе
    REGISTRATION_BUTTON = By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']/button"  # Кнопка Зарегистрироваться
    LOG_IN_BUTTON_2 = By.XPATH, "//*[@id='root']/div/main/div/form/button"  # Кнопка Войти на странице Вход
    FORM_ORDER = By.XPATH, ".//section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']/div/button"  # Кнопка Оформить заказ
    INCORRECT_PASS = By.XPATH, ".//fieldset[@class='Auth_fieldset__1QzWN mb-6']/div/p"  # Надпись Неверный пароль
    PERSONAL_INFO = By.XPATH, "//*[@id='root']/div/header/nav/a/p"  # Кнопка Личный кабинет
    LOG_IN_BUTTON_3 = By.XPATH, ".//a[@href='/login']"  # Кнопка Войти на странице формы регистрации\ восстановления пароля
    FORGOT_PASS = By.XPATH, ".//a[@href='/forgot-password']"  # Кнопка Забыли пароль?
    CHANGE_INFO = By.XPATH, "//*[@id='root']/div/main/div/nav/p"  # Надпись В этом разделе вы можете... на странице личного кабинета
    CONSTRUCTOR = By.XPATH, ".//p[text()='Конструктор']"  # Кнопка перехода в конструктор в верхнем меню
    LOGO = By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/a[@href='/']"  # Лого в верхнем меню
    LOG_OUT = By.XPATH, ".//button[text()='Выход']"  # Кнопка выхода в личном кабинете
    BUNS = By.XPATH, ".//span[text()='Булки']"  # Кнопка перехода к разделу Булки
    SAUCES = By.XPATH, ".//span[text()='Соусы']"  # Кнопка перехода к разделу Соусы
    FILLINGS = By.XPATH, ".//span[text()='Начинки']"  # Кнопка перехода к разделу Начинки
    BUNS_TEXT = By.XPATH, ".//h2[text()='Булки']"  # Надпись Булки внутри конструктора
    SAUCES_TEXT = By.XPATH, ".//h2[text()='Соусы']"  # Надпись Соусы внутри конструктора
    FILLINGS_TEXT = By.XPATH, ".//h2[text()='Начинки']"  # Надпись Начинки внутри конструктора
