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

PASSWORD_LETTER_VALID = [
        "abc",
        "aBC",
        "123a",
        ".,/a",
        "123ABC{[a]}"
    ]

PASSWORD_LETTER_INVALID = [
    "ABC",
    "123",
    "{[]}",
    "{ABC}[123]"
]


class TestAuth:
    def test_length_valid(self):
        for i in range(25):
            string = ""
            for _ in range(PasswordLength.MAX_LENGTH + i):
                random_index = random.randint(0, len(printable) - 1)
                string += printable[random_index]

            assert PasswordLength.test(string)

    def test_length_invalid(self):
        print(PASSWORD_LETTER_VALID)
        for i in range(25):
            string = ""
            for _ in range(PasswordLength.MAX_LENGTH - (i + 1)):
                random_index = random.randint(0, len(printable) - 1)
                string += printable[random_index]

            assert not PasswordLength.test(string)

    @pytest.mark.parametrize("password", PASSWORD_LETTER_VALID)
    def test_letter_valid(self, password):
        assert PasswordLetter.test(password)

    @pytest.mark.parametrize("password", PASSWORD_LETTER_INVALID)
    def test_letter_invalid(self, password):
        assert not PasswordLetter.test(password)


