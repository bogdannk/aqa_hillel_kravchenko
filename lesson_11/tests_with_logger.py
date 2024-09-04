import logging
from assertpy import assert_that
from lesson_11.homework_10 import log_event

class TestLogLevels:
    LOG_FILE = 'login_system.log'

    def setup_method(self):

        # Настройка логгера для тестов
        self.logger = logging.getLogger("log_event")
        self.logger.setLevel(logging.INFO)


        # Перехват сообщений
        self.log_messages = []
        self.handler = logging.Handler()
        self.handler.emit = self.log_messages.append  # Переопределение метода emit
        self.logger.addHandler(self.handler)

    def test_success_log(self):
        # Логируем успешный вход
        log_event("user1", "success")

        # Проверяем, что сообщение записано и уровень логирования правильный
        assert_that(self.log_messages).is_not_empty()
        assert_that(self.log_messages[0].levelname).is_equal_to('INFO')
        assert_that(self.log_messages[0].message).contains("Username: user1, Status: success")

    def test_expired_log(self):
        # Логируем событие с истекшим паролем
        log_event("user2", "expired")

        # Проверяем, что сообщение записано и уровень логирования правильный
        assert_that(self.log_messages).is_not_empty()
        assert_that(self.log_messages[0].levelname).is_equal_to('WARNING')
        assert_that(self.log_messages[0].message).contains("Username: user2, Status: expired")

    def test_failed_log(self):
        log_event("user3", "failed")

        # Проверяем, что сообщение записано и уровень логирования правильный
        assert_that(self.log_messages).is_not_empty()
        assert_that(self.log_messages[0].levelname).is_equal_to('ERROR')
        assert_that(self.log_messages[0].message).contains("Username: user3, Status: failed")