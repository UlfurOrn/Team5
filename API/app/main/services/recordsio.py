from abctable import *

class Recordsio(Abctable):
    """
        An input-output class for the records table in the Habit tracker database.
        Contains methods for each CRUD operation [GET, POST, PUT, DELETE]
    """
    @classmethod
    def get(cls, id: list):
        """ Takes in a list of ints. Returns row with set ints or all rows if list=[] """
        if id != []:
            super()._cur.execute("SELECT * FROM records WHERE userid = %s AND typeid = %s AND rdatetime = %s;", (id[0], id[1], id[2]))
        else:
            super()._cur.execute("SELECT * FROM records;")
        return super()._cur.fetchall()


    @classmethod
    def post(cls, data: dict):
        """ Takes in a dict with a user and saves to the database. Returns nothing """
        userid, typeid, rdatetime, ammount = data["UserId"], data["TypeId"], data["RDateTime"], data["Amount"]
        super()._cur.execute("INSERT INTO records VALUES (%s, %s, %s, %s);", (userid, typeid, rdatetime, ammount))


    @classmethod
    def put(cls, id: list, data: dict):
        """ Takes in a list of ints and a dict with info to change and updates those columns in the database. Returns nothing """
        values = [val for val in data.values()] # Get all keys from the input dict
        keys = [key for key in data.keys()]     # Get all values from the input dict
        values.extend(id)

        commandStr = "UPDATE records SET "
        for i in range(len(keys)):                      # Add all update arguments to the string
            commandStr += "{} = %s,".format(keys[i])
        commandStr = commandStr[:-1].replace(";", "")   # To avoid SQL injections and remove last comma
        commandStr += " WHERE userid = %s AND typeid = %s AND rdatetime = %s;" 

        super()._cur.execute(commandStr, values)


    @classmethod
    def delete(cls, id: list):
        """ Takes in a list of ints. Deletes row with those id's from the database. Returns nothing """
        super()._cur.execute("DELETE FROM users WHERE userid = %s AND typeid = %s AND rdatetime = %s;", (id[0], id[1], id[2]))





if __name__ == "__main__":
    """
    print(Recordsio.get([1, 1, '2020-09-03 10:05:26']))
    Recordsio.put([1, 1, '2020-09-03 10:05:26'], {"ammount": "1000"})
    print(Recordsio.get([1, 1, '2020-09-03 10:05:26']))
    print (Recordsio.get([]))
    """