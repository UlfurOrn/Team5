from main.util.mappers.mapper import Mapper


class McategoryMapper(Mapper):
    """
        A Mapper class for the MCategories table
    """
    KEYS = [
        "mcategoryid",
        "name"
    ]
