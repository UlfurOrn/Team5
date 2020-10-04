from main.repositories.abc_table import AbcTable
from main.util.mappers.usermapper import UserMapper
from psycopg2.extensions import AsIs  # Used to remove '' from SQL strings I insert


class UsersIO(AbcTable):
    """
        An input-output class for the users table in the Habit tracker database.
        Contains methods for each CRUD operation [GET, POST, PUT, DELETE]. Also
        provides a function checkpassword that checks if a username-password 
        combination matches in the database.
    """
    table = "users"
    table_key = "userid"

    @classmethod
    def get(cls, user_id=None):
        """ Takes in an int. Returns row from users with set id or all rows if id=None as list of User objects"""
        if user_id:
            super()._cur.execute("SELECT * FROM users WHERE userid = %s;", (user_id,))
        else:
            super()._cur.execute("SELECT * FROM users;")

        users_list = []
        for user_info in super()._cur.fetchall():
            user = UserMapper(*user_info)
            users_list.append(user)

        return users_list

    @classmethod
    def checkpassword(cls, username, password):
        """ Takes in a username and a password and checks if the username and password match in the database """
        super()._cur.execute("SELECT F_CheckPassword(%s, %s);", (password, username))
        return super()._cur.fetchall()
