from mapper import Mapper

class Measurement(Mapper):
    def __init__(self, measurementid=None, name=None, abreviation=None, mcategoryid=None):
        self.measurementid = measurementid
        self.name = name
        self.abreviation = abreviation
        self.mcategoryid = mcategoryid