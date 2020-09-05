from main.services.abc_table import AbcTable


class Typesio(AbcTable):
    """
        An input-output class for the types table in the Habit tracker database.
        Contains methods for each CRUD operation [GET, POST, PUT, DELETE]
    """
    @classmethod
    def get(cls, id):
        """ Takes in an int. Returns row from types with set id or all rows if id=None """
        if id:
            super()._cur.execute("SELECT * FROM types WHERE typeid = %s;", (id,))
        else:
            super()._cur.execute("SELECT * FROM types;")
        return super()._cur.fetchall()

    @classmethod
    def post(cls, data):
        """ Takes in a dict with a type and saves to the database. Returns nothing """
        name, description, measurement = data["Name"], data["Description"], data["Measurement"]
        super()._cur.execute("INSERT INTO types (name, description, measurement) VALUES (%s, %s, %s);", (name, description, measurement))

    @classmethod
    def put(cls, id, data):
        """ Takes in an int and a dict with info to change and updates those columns in the database. Returns nothing """
        values = [val for val in data.values()] # Get all keys from the input dict
        keys = [key for key in data.keys()]     # Get all values from the input dict
        values.extend([id])

        commandStr = "UPDATE types SET "
        for i in range(len(keys)):                      # Add all updates to string
            commandStr += "{} = %s,".format(keys[i])
        commandStr = commandStr[:-1].replace(";", "")   # To avoid SQL injections and remove last comma
        commandStr += " WHERE typeid = %s;" 

        super()._cur.execute(commandStr, values)

    @classmethod
    def delete(cls, id):
        """ Takes in an int. Deletes row with that id from the database. Returns nothing """
        super()._cur.execute("DELETE FROM types WHERE typeid = %s;", (id,))