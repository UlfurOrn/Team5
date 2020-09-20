from main.util.mappers.mapper import Mapper

class Measurement(Mapper):
    """
        A Mapper class for the Measurements table
    """
    def __init__(self, measurementid=None, name=None, abreviation=None, mcategoryid=None):
        self.measurementid = measurementid
        self.name = name
        self.abreviation = abreviation
        self.mcategoryid = mcategoryid