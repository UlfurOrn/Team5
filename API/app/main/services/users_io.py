from main.services.abc_table import AbcTable


class Usersio(AbcTable):
    """
        An input-output class for the users table in the Habit tracker database.
        Contains methods for each CRUD operation [GET, POST, PUT, DELETE]
    """
    @classmethod
    def get(cls, id):
        """ Takes in an int. Returns row from users with set id or all rows if id=None """
        if id:
            super()._cur.execute("SELECT * FROM users WHERE userid = %s;", (id,))
        else:
            super()._cur.execute("SELECT * FROM users;")
        print("Select")
        return super()._cur.fetchall()

    @classmethod
    def post(cls, data):
        """ Takes in a dict with a user and saves to the database. Returns nothing """
        name, email, dob, gender, weight, height = data["Name"], data["Email"], data["DoB"], data["Gender"], data["Weight"], data["Height"]
        super()._cur.execute("INSERT INTO users (Name, Email, DoB, Gender, Weight, Height) VALUES (%s, %s, %s, %s, %s, %s);",
            (name, email, dob, gender, weight, height))

    @classmethod
    def put(cls, id, data):
        """ Takes in an int and a dict with info to change and updates those columns in the database. Returns nothing """
        values = [val for val in data.values()] # Get all keys from the input dict
        keys = [key for key in data.keys()]     # Get all values from the input dict
        values.extend([id])

        commandStr = "UPDATE users SET "
        for i in range(len(keys)):                      # Add all updates to string
            commandStr += "{} = %s,".format(keys[i])
        commandStr = commandStr[:-1].replace(";", "")   # To avoid SQL injections and remove last comma
        commandStr += " WHERE userid = %s;" 

        super()._cur.execute(commandStr, values)

    @classmethod
    def delete(cls, id):
        """ Takes in an int. Deletes row with that id from the database. Returns nothing """
        super()._cur.execute("DELETE FROM users WHERE userid = %s;", (id,))