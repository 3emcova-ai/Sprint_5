import random

class Data:
    STELLAR_BURGERS_URL = "https://stellarburgers.education-services.ru/"

    NAME = "Inna"
    SURNAME = "Zemtsova"
    NUMBER_COHORT = "53"
    DOMAIN = "@yandex.ru"
    PASSWORD = "Qaz12345"

    @staticmethod
    def email_generation():
        return f"{Data.NAME}_{Data.SURNAME}_{Data.NUMBER_COHORT}_{random.randint(100, 999)}{Data.DOMAIN}"


    