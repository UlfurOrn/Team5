from abc import ABC


class AuthInterface(ABC):
    """Interface that Authentication Plugins need to implement"""

    @classmethod
    def test(cls, password: str) -> bool:
        pass
