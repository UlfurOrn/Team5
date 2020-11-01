from main.util.authentication.authentication_plugins import (
    PasswordLength,
    PasswordLetter,
    PasswordCapital,
    PasswordNumber,
    PasswordSpecial
)


class AuthTest:
    MIN_SECURITY_LEVEL = 3  # Number of valid plugins for password to be valid

    # A list of plugins that test a passwords strength, each one implements
    # the AuthInterface.
    PLUGIN_LIST = [
        PasswordLength,
        PasswordLetter,
        PasswordCapital,
        PasswordNumber,
        PasswordSpecial
    ]

    @classmethod
    def valid_password(cls, password):
        """Tests a passwords security level and if it reaches the
        specified MIN_SECURITY_LEVEL benchmark
        """
        security_level = 0
        for plugin in cls.PLUGIN_LIST:
            if plugin.test(password):
                security_level += 1

        return security_level >= cls.MIN_SECURITY_LEVEL
