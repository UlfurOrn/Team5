from main.util.mappers.mapper import Mapper


class Record(Mapper):
    """
        A Mapper class for the Records table
    """
    def __init__(self, recordid=None, userid=None, habitid=None, amount=None, rdate=None, rtime=None):
        self.recordid = recordid
        self.userid = userid
        self.habitid = habitid
        self.amount = amount
        self.rdate = rdate
        self.rtime = rtime