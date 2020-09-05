from abctable import *

class Typesio(Abctable):
    """
        An input-output class for the types table in the Habit tracker database.
        Contains methods for each CRUD operation [GET, POST, PUT, DELETE]
    """
    @classmethod
    def get(cls, id):
        if id:
            super()._cur.execute("SELECT * FROM types WHERE typeid = %s;", (id,))
        else:
            super()._cur.execute("SELECT * FROM types;")
        return super()._cur.fetchall()

    @classmethod
    def post(cls, data):
        name, description, measurement = data["Name"], data["Description"], data["Measurement"]
        super()._cur.execute("INSERT INTO types (name, description, measurement) VALUES (%s, %s, %s);", (name, description, measurement))

    @classmethod
    def put(cls, id, data):
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
        super()._cur.execute("DELETE FROM types WHERE typeid = %s;", (id,))

if __name__ == "__main__":
    """
    print(Typesio.get(None))
    Typesio.post({"Name": "TestType", "Description":"A test type", "Measurement": "TestCoverage"})
    print(Typesio.get(None))
    Typesio.put(4, {"Name":"TestType2", "Description": "Test type 2"})
    print(Typesio.get(None))
    Typesio.delete(4)
    print(Typesio.get(None))
    """