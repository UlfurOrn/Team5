from main.services.abc_table import AbcTable
from main.util.mappers.habit import Habit


class Habitsio(AbcTable):
    """
        An input-output class for the habits table in the Habit tracker database.
        Contains methods for each CRUD operation [GET, POST, PUT, DELETE]
    """
    @classmethod
    def get(cls, habit_id):
        """ Takes in an int. Returns row from habits with set id or all rows if id=None """
        if habit_id:
            super()._cur.execute("SELECT * FROM habits WHERE habitid = %s;", (habit_id,))
        else:
            super()._cur.execute("SELECT * FROM habits;")
        habits_list = []
        for habit in super()._cur.fetchall():
            habits_list.append(Habit(habit[0], habit[1], habit[2], habit[3], habit[4]))
        return habits_list

    @classmethod
    def post(cls, data):
        """ Takes in a dict with a type and saves to the database. Returns nothing """
        name, description, measurement = data["name"], data["description"], data["measurement"]
        super()._cur.execute("INSERT INTO types (name, description, measurement) VALUES (%s, %s, %s);", (name, description, measurement))

    @classmethod
    def put(cls, habit_id, data):
        """ Takes in an int and a dict with info to change and updates those columns in the database. Returns nothing """
        values = [val for val in data.values()] # Get all keys from the input dict
        keys = [key for key in data.keys()]     # Get all values from the input dict
        values.extend([habit_id])

        commandStr = "UPDATE habits SET "
        for i in range(len(keys)):                      # Add all updates to string
            commandStr += "{} = %s,".format(keys[i])
        commandStr = commandStr[:-1].replace(";", "")   # To avoid SQL injections and remove last comma
        commandStr += " WHERE habitid = %s;" 

        super()._cur.execute(commandStr, values)

    @classmethod
    def delete(cls, habit_id):
        """ Takes in an int. Deletes row with that id from the database. Returns nothing """
        super()._cur.execute("DELETE FROM habits WHERE habitid = %s;", (habit_id,))