from main.util.mappers.habitmapper import HabitMapper
from main.util.mappers.usermapper import UserMapper
from main.util.mappers.recordmapper import RecordMapper

class DBapi():
    """
        A class that satisfies the Dependency Injection. Takes in a Database api
        in the constructor which it then uses in alls its functions. Makes it easier
        to change out different database apis.
    """
    def __init__(self, DatabaseApi):
        self.dbapi = DatabaseApi

    def users(self, method: str, user_id: int = None, data: UserMapper = None):
        """
            A gateway to the users data.
            Arguments:
                method: str - Specifies the method to use [GET, POST, PUT, DELETE]
                user_id: int - Specifies the id of the object. If none, gets all in GET method
                data: Object of type User to be used for insert or update
            Returns:
                If method = GET returns list of User objects else returns nothing
        """
        return self.dbapi.users(method, user_id, data)

    def habits(self, method: str, habit_id: int = None, data: HabitMapper = None):
        """
            A gateway to the habits data.
            Arguments:
                method: str - Specifies the method to use [GET, POST, PUT, DELETE]
                habit_id: int - Specifies the id of the object. If none, gets all in GET method
                data: Object of type Habit to be used for insert or update
            Returns:
                If method = GET returns list of Habit objects else returns nothing
        """
        return self.dbapi.habits(method, habit_id, data)

    def records(self, method: str, record_id: int = None, data: RecordMapper = None):
        """
            A gateway to the records data.
            Arguments:
                method: str - Specifies the method to use [GET, POST, PUT, DELETE]
                record_id: int - Specifies the id of the object. If none, gets all in GET method
                data: Object of type Record to be used for insert or update
            Returns:
                If method = GET returns list of Record objects else returns nothing
        """
        return self.dbapi.records(method, record_id, data)

    def measurements(self, measurement_id: int = None):
        """
        A gateway to the measurements data.
            Argument: measurement_id: int- Specifies the id of the object. If none, gets all in GET method
            Returns: row with id or all rows if id is none as list of Measurement objects
        """
        return self.dbapi.measurements(measurement_id)

    def mcategories(self, category_id: int = None):
        """
        A gateway to the mcategories data.
            Argument: category_id: int- Specifies the id of the object. If none, gets all in GET method
            Returns: row with id or all rows if id is none as list of Mcategories objects
        """
        return self.dbapi.mcategories(category_id)
    
    def checkpassword(self, username: str, password: str):
        """ Takes in a username and password and checks if they match in the database """
        return self.dbapi.checkpassword(username, password)
