from main.util.mappers.mapper import Mapper


class Habit(Mapper):
    """
        A Mapper class for the Habits table
    """
    KEYS = ["habitid", "userid", "name", "description", "measurementid"]
