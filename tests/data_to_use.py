import random


class TestData:
    REG_NAME = "Серафима"  # Имя, которое используется при регистрации
    RANDOM_EMAIL = f"serafima_timkova_6_{random.randint(100, 999)}@yandex.com"  # Рандомно созданный имейл для регистрации
    REG_PASS = "tHisIS1"  # Пароль, который используется при регистрации
    INCORRECT_PASS = "123"  # Некорректный пароль, который используется при регистрации
    EMAIL = "serafima_timkova_6_123@yandex.com"  # Имейл, который используется для аутентификации
    PASS = "tHisIS"  # Пароль, который используется для аутентификации
    LOG_IN_PAGE = "https://stellarburgers.nomoreparties.site/login"  # Страница логина
    REG_PAGE = "https://stellarburgers.nomoreparties.site/register"  # Страница регистрации
