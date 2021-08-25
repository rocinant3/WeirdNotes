from .base import BaseExceptionCase


class AccountException:

    class UserCreate(BaseExceptionCase):
        message = "Ошибка создания аккаунта"

        def __init__(self, status_code: int = 500):
            BaseExceptionCase.__init__(self, status_code, self.message)

    class Authorize(BaseExceptionCase):
        message = "Ошибка авторизации"

        def __init__(self, status_code: int = 500):
            BaseExceptionCase.__init__(self, status_code, self.message)
