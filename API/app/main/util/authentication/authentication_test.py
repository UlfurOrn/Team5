from main.util.authentication.authentication_plugins import (
    PasswordLength,
    PasswordLetter,
    PasswordCapital,
    PasswordNumber,
    PasswordSpecial
)


class AuthTest:
    MIN_SECURITY_LEVEL = 3
    PLUGIN_LIST = []

    @classmethod
    def check_password(cls, password):
        security_level = 0
        for plugin in cls.PLUGIN_LIST:
            security_level += plugin.test(password)

        return security_level >= cls.MIN_SECURITY_LEVEL
