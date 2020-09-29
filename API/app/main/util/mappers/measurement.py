from main.util.mappers.mapper import Mapper


class Measurement(Mapper):
    """
        A Mapper class for the Measurements table
    """
    KEYS = ["measurementid", "name", "abreviation", "mcategoryid"]
