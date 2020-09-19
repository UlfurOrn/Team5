from mapper import Mapper

class record(Mapper):
    def __init__(self, recordid=None, userid=None, habitid=None, amount=None, rdate=None, rtime=None):
        self.recordid = recordid
        self.userid = userid
        self.habitid = habitid
        self.amount = amount
        self.rdate = rdate
        self.rtime = rtime
