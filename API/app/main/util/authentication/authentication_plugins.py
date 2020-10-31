from string import punctuation

from main.util.authentication.authentication_interface import AuthInterface


class PasswordLength(AuthInterface):
    MAX_LENGTH = 10

    @classmethod
    def test(cls, password):
        return len(password) >= cls.MAX_LENGTH


class PasswordLetter(AuthInterface):
    @classmethod
    def test(cls, password):
        for c in password:
            if c.islower():
                return True
        return False


class PasswordCapital(AuthInterface):
    @classmethod
    def test(cls, password):
        for c in password:
            if c.isupper():
                return True
        return False


class PasswordNumber(AuthInterface):
    @classmethod
    def test(cls, password):
        for c in password:
            if c.isdigit():
                return True
        return False


class PasswordSpecial(AuthInterface):
    @classmethod
    def test(cls, password):
        for c in password:
            if c in punctuation:
                return True
        return False
