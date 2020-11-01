from string import punctuation

from main.util.authentication.authentication_interface import AuthInterface


class PasswordLength(AuthInterface):
    """Check that a password is at least MAX_LENGTH characters long"""
    MAX_LENGTH = 10

    @classmethod
    def test(cls, password):
        return len(password) >= cls.MAX_LENGTH


class PasswordLetter(AuthInterface):
    """Checks that a password has at least 1 lowercase letter"""
    @classmethod
    def test(cls, password):
        for c in password:
            if c.islower():
                return True
        return False


class PasswordCapital(AuthInterface):
    """Checks that a password has at least 1 capital letter"""
    @classmethod
    def test(cls, password):
        for c in password:
            if c.isupper():
                return True
        return False


class PasswordNumber(AuthInterface):
    """Checks that a password has at least 1 number"""
    @classmethod
    def test(cls, password):
        for c in password:
            if c.isdigit():
                return True
        return False


class PasswordSpecial(AuthInterface):
    """Checks that a password has at least 1 special character"""
    @classmethod
    def test(cls, password):
        for c in password:
            if c in punctuation:
                return True
        return False
