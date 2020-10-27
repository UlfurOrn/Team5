from abc import ABC


class AuthInterface(ABC):

    @classmethod
    def test(cls, password: str) -> bool:
        pass
