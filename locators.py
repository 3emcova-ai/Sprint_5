from selenium.webdriver.common.by import By


class Locators:
#главная страница
    PERSONAL_ACCOUNT = (By.XPATH, ".//p[text()='Личный Кабинет']")  #кнопка входа в личный кабинет
    MAIN_PAGE_LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # кнопка Войти в аккаунт
    PLACE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")   #кнопка Оформить заказ
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")  #кнопка Конструктор
    CONSTRUCTOR_SECTION = (By.XPATH, ".//h1[text()='Соберите бургер']")  #раздел Конструктор
    BUNS_BUTTON = (By.XPATH, ".//span[text()='Булки']")  #кнопка Булки
    BUNS_SECTION = (By.XPATH, ".//h2[text()='Булки']")  #раздел Булки
    SAUCES_BUTTON = (By.XPATH, ".//span[text()='Соусы']")  #кнопка Соусы
    SAUCES_SECTION = (By.XPATH, ".//h2[text()='Соусы']")  #раздел Соусы
    TOPPINGS_BUTTON = (By.XPATH, ".//span[text()='Начинки']")  #кнопка Начинки
    TOPPINGS_SECTION = (By.XPATH, ".//h2[text()='Начинки']")  #раздел Начинки
#форма регистрации и входа
    REGISTRATION_LINK = (By.XPATH, ".//a[text()='Зарегистрироваться']")  #ссылка для регистрации
    NAME_FIELD = (By.XPATH, "(.//input[@name='name'])[1]")  #поле ввода имени
    REG_EMAIL_FIELD = (By.XPATH, "(.//input[@name='name'])[2]") #поле ввода почты при регистрации
    PASSWORD_FIELD = (By.XPATH, ".//input[@name='Пароль']") #поле ввода пароля
    BUTTON_REGISTRATION = (By.XPATH, ".//button[text()='Зарегистрироваться']") #кнопка регистрации
    ERROR_INVALID_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']")  #ошибка регистрации при вводе некорректного пароля
    LOG_EMAIL_FIELD = (By.XPATH, "(.//input[@name='name'])") #поле ввода почты зарегистрированного пользователя
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']") #кнопка входа зарегистрированного пользователя
    PASSWORD_RECOVERY_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")  #ссылка для восстановления пароля
    LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")  #ссылка для входа в форме восстановления пароля
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']") #кнопка выхода зарегистрированного пользователя
#личный кабинет
    PROFILE = (By.XPATH, ".//a[text()='Профиль']")  #надпись "Профиль" в личном кабинете
    