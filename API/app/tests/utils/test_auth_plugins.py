import unittest
import pytest
import random
from string import printable

from main.util.authentication.authentication_plugins import (
    PasswordLength,
    PasswordLetter,
    PasswordCapital,
    PasswordNumber,
    PasswordSpecial
)


class TestAuth(unittest.TestCase):

    def test_length_valid(self):
        for i in range(25):
            string = ""
            for _ in range(PasswordLength.MAX_LENGTH + i):
                random_index = random.randint(0, len(printable) - 1)
                string += printable[random_index]

            assert PasswordLength.test(string)

    def test_length_invalid(self):
        for i in range(25):
            string = ""
            for _ in range(PasswordLength.MAX_LENGTH - (i + 1)):
                random_index = random.randint(0, len(printable) - 1)
                string += printable[random_index]

            assert not PasswordLength.test(string)




