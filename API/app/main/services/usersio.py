from abctable import *

class Usersio(Abctable):
    """
        An input-output class for the users table in the Habit tracker database.
        Contains methods for each CRUD operation [GET, POST, PUT, DELETE]
    """
    @classmethod
    def get(cls, id):
        if id:
            super()._cur.execute("SELECT * FROM users WHERE userid = %s;", (id,))
        else:
            super()._cur.execute("SELECT * FROM users;")
        return super()._cur.fetchall()

    @classmethod
    def post(cls, data):
        name, email, dob, gender, weight, height = data["Name"], data["Email"], data["DoB"], data["Gender"], data["Weight"], data["Height"]
        super()._cur.execute("INSERT INTO users (Name, Email, DoB, Gender, Weight, Height) VALUES (%s, %s, %s, %s, %s, %s);",
            (name, email, dob, gender, weight, height))

    @classmethod
    def put(cls, id, data):
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
        super()._cur.execute("DELETE FROM users WHERE userid = %s;", (id,))

if __name__ == "__main__":
    """
    print(Usersio.get(None))
    #Usersio.post({"Name": "Testio", "Email":"testio@tes.is", "DoB":"2020-01-01", "Gender":"f", "Weight":70, "Height":170})
    Usersio.put(5, {"Name": "TestIO", "Gender":"f"})
    print(Usersio.get(None))
    """
