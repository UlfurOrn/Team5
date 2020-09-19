from main.util.mappers.mapper import Mapper

class Mcategory(Mapper):
    def __init__(self, mcategoryid=None, name=None):
        self.mcategoryid = mcategoryid
        self.name = name