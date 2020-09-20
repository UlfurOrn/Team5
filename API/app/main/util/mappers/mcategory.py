from main.util.mappers.mapper import Mapper

class Mcategory(Mapper):
    """
        A Mapper class for the MCategories table
    """
    def __init__(self, mcategoryid=None, name=None):
        self.mcategoryid = mcategoryid
        self.name = name