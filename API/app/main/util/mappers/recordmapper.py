from main.util.mappers.mapper import Mapper


class RecordMapper(Mapper):
    """
        A Mapper class for the Records table
    """
    KEYS = [
        "recordid",
        "userid",
        "habitid",
        "amount",
        "rdate",
        "rtime"
    ]
