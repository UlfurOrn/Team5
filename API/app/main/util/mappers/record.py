from main.util.mappers.mapper import Mapper


class Record(Mapper):
    """
        A Mapper class for the Records table
    """
    KEYS = ["recordid", "userid", "habitid", "amount", "rdate", "rtime"]
