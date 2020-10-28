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

PASSWORD_CAPITAL_VALID = [
    "ABC",
    "Abc",
    "123A",
    "{[A]}",
    "123abc{[A]}"
]

PASSWORD_CAPITAL_INVALID = [
    "abc",
    "123",
    "{[]}",
    "{abc}[123]"
]

PASSWORD_NUMBER_VALID = [
    "123",
    "1abc",
    "ABC1",
    "{[1]}",
    "ABCabc{[1]}"
]

PASSWORD_NUMBER_INVALID = [
    "abc",
    "ABC",
    "{[]}",
    "{abc}[ABC]"
]

PASSWORD_SPECIAL_VALID = [
    "{[]}",
    "a{b}c",
    "[123]",
    "123.abc",
    "ABC123/abc123"
]

PASSWORD_SPECIAL_INVALID = [
    "abc",
    "ABC",
    "123",
    "abc123ABC"
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

    @pytest.mark.parametrize("password", PASSWORD_CAPITAL_VALID)
    def test_capital_valid(self, password):
        assert PasswordCapital.test(password)

    @pytest.mark.parametrize("password", PASSWORD_CAPITAL_INVALID)
    def test_capital_invalid(self, password):
        assert not PasswordCapital.test(password)

    @pytest.mark.parametrize("password", PASSWORD_NUMBER_VALID)
    def test_number_valid(self, password):
        assert PasswordNumber.test(password)

    @pytest.mark.parametrize("password", PASSWORD_NUMBER_INVALID)
    def test_number_invalid(self, password):
        assert not PasswordNumber.test(password)

    @pytest.mark.parametrize("password", PASSWORD_SPECIAL_VALID)
    def test_special_valid(self, password):
        assert PasswordSpecial.test(password)

    @pytest.mark.parametrize("password", PASSWORD_SPECIAL_INVALID)
    def test_special_invalid(self, password):
        assert not PasswordSpecial.test(password)
