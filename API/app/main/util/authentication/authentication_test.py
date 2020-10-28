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
    def valid_password(cls, password):
        security_level = 0
        for plugin in cls.PLUGIN_LIST:
            if plugin.test(password):
                security_level += 1

        return security_level >= cls.MIN_SECURITY_LEVEL
