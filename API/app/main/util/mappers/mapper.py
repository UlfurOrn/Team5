class Mapper():
    """ 
        This is a mapper super class for sql-rest transactions that defines four functions.
        __str__ returns a string of the objects for testing purposes
        to_dict returns the class as a dict object for the REST-api to turn into JSON
        to_sql_update returns a string that can be used in an sql update query
        to_sql_insert returns a touble of strings that can be used in an sql insert query
    """
    def __str__(self):
        return str(self.__dict__)

    def to_dict(self):
        return self.__dict__

    def set_dict(self, input_dict):
        self.__dict__ = input_dict

    def to_sql_update(self):
        """ Returns a string for an sql update query """
        ret_str = ""
        for key, value in self.__dict__.items():
            if value != None:
                ret_str += "{} = '{}', ".format(key, value)
        return ret_str.strip(", ")
    
    def to_sql_insert(self):
        """ Returns a touble of strings that can be used in an sql insert query """
        keys_str = "("
        values_str = "("
        for key, value in self.__dict__.items():
            if value != None:
                keys_str += "{}, ".format(key)
                values_str += "'{}', ".format(value)
        return (keys_str.strip(", ") + ")", values_str.strip(", ") + ")")