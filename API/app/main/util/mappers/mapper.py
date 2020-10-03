class Mapper:
    """
        This is a mapper super class (or Layer Supertype) for sql-rest transactions that defines five functions.
        __str__ returns a string of the objects for testing purposes
        to_dict returns the class as a dict object for the REST-api to turn into JSON
        set_dict sets the __dict__ variable of the mapper to a json body
        to_sql_update returns a string that can be used in an sql update query
        to_sql_insert returns a tuple of strings that can be used in an sql insert query
    """
    def __init__(self, *args, **kwargs):
        self.parse_input(self.KEYS, *args, **kwargs)

    def parse_input(self, keys, *args, **kwargs):
        info_dict = kwargs
        if args:
            for key, value in zip(keys, args):
                info_dict[key] = value

        self.__dict__ = info_dict

    def __str__(self):
        return str(self.__dict__)

    def to_dict(self):
        return self.__dict__

    def set_dict(self, input_dict):
        self.__dict__ = input_dict

    def to_sql_update(self):
        """ Returns a string for an sql update query """
        sql_string_list = []

        for key, value in self.__dict__.items():
            if value is not None:
                sql_string_list.append(f"{key} = '{value}'")

        return ", ".join(sql_string_list)

    def to_sql_insert(self):
        """ Returns a tuple of strings that can be used in an sql insert query """
        key_string_list = []
        value_string_list = []

        for key, value in self.__dict__.items():
            if value is not None:
                key_string_list.append(key)
                value_string_list.append(f"'{value}'")

        key_string = "({})".format(", ".join(key_string_list))
        value_string = "({})".format(", ".join(value_string_list))

        return key_string, value_string
