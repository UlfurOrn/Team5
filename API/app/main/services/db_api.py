from main.services.users_io import Usersio
from main.services.records_io import Recordsio
from main.services.types_io import Typesio


class DBapi():
    """
        A gateway class that interfaces the database operations available for the Habit tracker platform.
        Each method is a table in the database. So adding a new table requires the addition of a new method.
    """
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    
    @classmethod
    def users(cls, method: str, id: int=None, data: dict=None):
        """ 
            A gateway to the users table.
            Arguments: 
                method: str - Specifies the method to use [GET, POST, PUT, DELETE]
                id: int - Specifies the id of the object. If none, gets all in GET method
                data: Dictionary of data to be written or updated in the database
            Returns:
                If method = GET returns list of dictionaries else returns nothing
        """
        if method == cls.GET:
            return Usersio.get(id)

        elif method == cls.POST:
            if data:
                Usersio.post(data)
            else:
                raise Exception("Missing data")

        elif method == cls.PUT:
            if id:
                if data:
                    Usersio.put(id, data)
                else:
                    raise Exception("Missing data")
            else:
                raise Exception("Missing id")

        elif method == cls.DELETE:
            if id:
                Usersio.delete(id)
            else:
                raise Exception("Missing id")

        else:
            raise Exception("Method not in list of approved methods: GET, POST, PUT, DELETE")

    @classmethod
    def types(cls, method: str, id: int=None, data: dict=None):
        """ 
            A gateway to the types table.
            Arguments: 
                method: str - Specifies the method to use [GET, POST, PUT, DELETE]
                id: int - Specifies the id of the object. If none, gets all in GET method
                data: Dictionary of data to be written or updated in the database
            Returns:
                If method = GET returns list of dictionaries else returns nothing
        """
        if method == cls.GET:
            return Typesio.get(id)

        elif method == cls.POST:
            if data:
                Typesio.post(data)
            else:
                raise Exception("Missing data")

        elif method == cls.PUT:
            if id:
                if data:
                    Typesio.put(id, data)
                else:
                    raise Exception("Missing data")
            else:
                raise Exception("Missing id")

        elif method == cls.DELETE:
            if id:
                Typesio.delete(id)
            else:
                raise Exception("Missing id")

        else:
            raise Exception("Method not in list of approved methods: GET, POST, PUT, DELETE")

    @classmethod
    def records(cls, method: str, ids: list=[], data: dict=None):
        """ 
            A gateway to the records table.
            Arguments: 
                method: str - Specifies the method to use [GET, POST, PUT, DELETE]
                id: list of ints - Specifies the ids of the object. If none, gets all in GET method
                data: Dictionary of data to be written or updated in the database
            Returns:
                If method = GET returns list of dictionaries else returns nothing
        """
        if method == cls.GET:
            return Recordsio.get(ids)

        elif method == cls.POST:
            if data:
                Recordsio.post(data)
            else:
                raise Exception("Missing data")

        elif method == cls.PUT:
            if ids:
                if data:
                    Recordsio.put(ids, data)
                else:
                    raise Exception("Missing data")
            else:
                raise Exception("Missing id")

        elif method == cls.DELETE:
            if ids:
                Recordsio.delete(ids)
            else:
                raise Exception("Missing id")

        else:
            raise Exception("Method not in list of approved methods: GET, POST, PUT, DELETE")