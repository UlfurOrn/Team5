from mapper import Mapper

class Habit(Mapper):
    def __init__(self, mcategoryid=None, name=None):
        self.mcategoryid = mcategoryid
        self.name = name