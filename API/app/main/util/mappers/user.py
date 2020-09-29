from main.util.mappers.mapper import Mapper


class User(Mapper):
    """
        A Mapper class for the Users table
    """
    KEYS = [
        "userid",
        "name",
        "email",
        "username",
        "password",
        "dob",
        "gender",
        "weight",
        "height"
    ]
