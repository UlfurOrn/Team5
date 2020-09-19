from main.services.users_io import Usersio
from main.services.records_io import Recordsio
from main.services.habits_io import Habitsio
from main.services.measurements_io import Measurementsio
from main.services.mcategories_io import Mcategoriesio

from main.util.mappers.habit import Habit
from main.util.mappers.user import User
from main.util.mappers.record import Record
from main.util.mappers.measurement import Measurement
from main.util.mappers.mcategory import Mcategory


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
    def users(cls, method: str, id: int=None, data: User=None):
        """ 
            A gateway to the users table.
            Arguments: 
                method: str - Specifies the method to use [GET, POST, PUT, DELETE]
                id: int - Specifies the id of the object. If none, gets all in GET method
                data: Object of type User to be used for insert or update
            Returns:
                If method = GET returns list of User objects else returns nothing
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
    def habits(cls, method: str, id: int=None, data: Habit=None):
        """ 
            A gateway to the habits table.
            Arguments: 
                method: str - Specifies the method to use [GET, POST, PUT, DELETE]
                id: int - Specifies the id of the object. If none, gets all in GET method
                data: Object of type Habit to be used for insert or update
            Returns:
                If method = GET returns list of Habit objects else returns nothing
        """
        if method == cls.GET:
            return Habitsio.get(id)

        elif method == cls.POST:
            if data:
                Habitsio.post(data)
            else:
                raise Exception("Missing data")

        elif method == cls.PUT:
            if id:
                if data:
                    Habitsio.put(id, data)
                else:
                    raise Exception("Missing data")
            else:
                raise Exception("Missing id")

        elif method == cls.DELETE:
            if id:
                Habitsio.delete(id)
            else:
                raise Exception("Missing id")

        else:
            raise Exception("Method not in list of approved methods: GET, POST, PUT, DELETE")

    @classmethod
    def records(cls, method: str, id: int=None, data: Record=None):
        """ 
            A gateway to the records table.
            Arguments: 
                method: str - Specifies the method to use [GET, POST, PUT, DELETE]
                id: int - Specifies the id of the object. If none, gets all in GET method
                data: Object of type Record to be used for insert or update
            Returns:
                If method = GET returns list of Record objects else returns nothing
        """
        if method == cls.GET:
            return Recordsio.get(id)

        elif method == cls.POST:
            if data:
                Recordsio.post(data)
            else:
                raise Exception("Missing data")

        elif method == cls.PUT:
            if id:
                if data:
                    Recordsio.put(id, data)
                else:
                    raise Exception("Missing data")
            else:
                raise Exception("Missing id")

        elif method == cls.DELETE:
            if id:
                Recordsio.delete(id)
            else:
                raise Exception("Missing id")

        else:
            raise Exception("Method not in list of approved methods: GET, POST, PUT, DELETE")
    
    @classmethod
    def measurements(cls, id: int=None):
        """
        A gateway to the measurements table.
            Argument: id: int- Specifies the id of the object. If none, gets all in GET method
            Returns: row with id or all rows if id is none as list of Measurment objects
        """
        return Measurementsio.get(id)

    @classmethod
    def mcategories(cls, id: int=None):
        """
        A gateway to the mcategories table.
            Argument: id: int- Specifies the id of the object. If none, gets all in GET method
            Returns: row with id or all rows if id is none as list of Mcategories objects
        """
        return Mcategoriesio.get(id)
    
    @classmethod
    def checkpassword(cls, username: str, password: str):
        """ Takes in a username and password and checks if they match in the database """
        return Usersio.password(username, password)