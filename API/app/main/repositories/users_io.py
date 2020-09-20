from main.repositories.abc_table import AbcTable
from main.util.mappers.user import User
from psycopg2.extensions import AsIs # Used to remove '' from SQL strings I insert

class Usersio(AbcTable):
    """
        An input-output class for the users table in the Habit tracker database.
        Contains methods for each CRUD operation [GET, POST, PUT, DELETE]
    """

    @classmethod
    def get(cls, user_id):
        """ Takes in an int. Returns row from users with set id or all rows if id=None as list of User objects"""
        if user_id:
            super()._cur.execute("SELECT * FROM users WHERE userid = %s;", (user_id,))
        else:
            super()._cur.execute("SELECT * FROM users;")
        users_list = []
        for user in super()._cur.fetchall():
            users_list.append(User(user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8]))
        return users_list

    @classmethod
    def post(cls, data):
        """ Takes in a dict with a user and saves to the database. Returns nothing """
        user_touple = data.to_sql_insert()
        super()._cur.execute("INSERT INTO users %s VALUES %s;", (AsIs(user_touple[0]), AsIs(user_touple[1])))

    @classmethod
    def put(cls, user_id, data):
        """ Takes in a Habit object and saves it to the database. Returns nothing """
        user_str = data.to_sql_update()
        super()._cur.execute("UPDATE users SET %s WHERE userid = %s", (AsIs(user_str), user_id))

    @classmethod
    def delete(cls, user_id):
        """ Takes in an int. Deletes row with that id from the database. Returns nothing """
        super()._cur.execute("DELETE FROM users WHERE userid = %s;", (user_id,))
    
    @classmethod
    def password(cls, username, password):
        """ Takes in a username and a password and checks if the username and password match in the database """
        super()._cur.execute("SELECT F_CheckPassword(%s, %s);", (password, username))
        return super()._cur.fetchall()
