from selenium.webdriver.common.by import By

class Locators:
    PERSONAL_ACCOUNT = (By.XPATH, ".//p[text()='Личный Кабинет']")  #кнопка входа в личный кабинет
    REGISTRATION_LINK = (By.XPATH, ".//a[text()='Зарегистрироваться']")  #ссылка для регистрации
    #форма регистрации
    NAME_FIELD = (By.XPATH, "(.//input[@name='name'])[1]")  #поле ввода имени
    EMAIL_FIELD = (By.XPATH, "(.//input[@name='name'])[2]") #поле ввода почты
    PASSWORD_FIELD = (By.XPATH, ".//input[@name='Пароль']") #поле ввода пароля
    BUTTON_REGISTRATION = (By.XPATH, ".//button[text()='Зарегистрироваться']") #кнопка регистрации
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']") #кнопка входа после успешной регистрации



    #Inna_Zemtsova_53_978@yandex.ru