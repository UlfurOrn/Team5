class Mapper:
    """ 
        This is a mapper super class (or Layer Supertype) for sql-rest transactions that defines five functions.
        __str__ returns a string of the objects for testing purposes
        to_dict returns the class as a dict object for the REST-api to turn into JSON
        set_dict sets the __dict__ variable of the mapper to a json body
        to_sql_update returns a string that can be used in an sql update query
        to_sql_insert returns a tuple of strings that can be used in an sql insert query
    """
    def __str__(self):
        return str(self.__dict__)

    def to_dict(self):
        return self.__dict__

    def set_dict(self, input_dict):
        self.__dict__ = input_dict

    def to_sql_update(self):
        """ Returns a string for an sql update query """
        sql_string_list = [
            f"{key} = '{value}'"
            for key, value in self.__dict__.items()
            if value is not None
        ]
        return ", ".join(sql_string_list)
    
    def to_sql_insert(self):
        """ Returns a tuple of strings that can be used in an sql insert query """
        key_string_list = [str(key) for key in self.__dict__.keys()]
        value_string_list = [f"'{value}'" for value in self.__dict__.values() if value is not None]

        key_string = "({})".format(", ".join(key_string_list))
        value_string = "({})".format(", ".join(value_string_list))

        return key_string, value_string
