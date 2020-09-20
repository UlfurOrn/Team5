from main.util.mappers.mapper import Mapper


class Habit(Mapper):
    """
        A Mapper class for the Habits table
    """
    def __init__(self, habitid=None, userid=None, name=None, description=None, measurementid=None):
        self.habitid = habitid
        self.userid = userid
        self.name = name
        self.description = description
        self.measurementid = measurementid