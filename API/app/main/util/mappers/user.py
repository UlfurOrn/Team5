from main.util.mappers.mapper import Mapper


class User(Mapper):
    """
        A Mapper class for the Users table
    """
    def __init__(self, userid=None, name=None, email=None, username=None, password=None, dob=None, gender=None, weight=None, height=None):
        self.userid = userid
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.dob = dob
        self.gender = gender
        self.weight = weight
        self.height = height
