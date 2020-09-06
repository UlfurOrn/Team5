from main.services.abc_table import AbcTable


class Recordsio(AbcTable):
    """
        An input-output class for the records table in the Habit tracker database.
        Contains methods for each CRUD operation [GET, POST, PUT, DELETE]
    """
    @classmethod
    def get(cls, record_id: list):
        """ Takes in a list of ints. Returns row from records with set id's or all rows if id=[] """
        if id != []:
            super()._cur.execute("SELECT * FROM records WHERE userid = %s AND typeid = %s AND rdatetime = %s;", (record_id[0], record_id[1], record_id[2]))
        else:
            super()._cur.execute("SELECT * FROM records;")
        return super()._cur.fetchall()


    @classmethod
    def post(cls, data: dict):
        """ Takes in a dict with a record and saves to the database. Returns nothing """
        userid, typeid, rdatetime, ammount = data["UserId"], data["TypeId"], data["RDateTime"], data["Amount"]
        super()._cur.execute("INSERT INTO records VALUES (%s, %s, %s, %s);", (userid, typeid, rdatetime, ammount))


    @classmethod
    def put(cls, record_id: list, data: dict):
        """ Takes in a list of ints and a dict with info to change and updates those columns in the database. Returns nothing """
        values = [val for val in data.values()] # Get all keys from the input dict
        keys = [key for key in data.keys()]     # Get all values from the input dict
        values.extend(record_id)

        commandStr = "UPDATE records SET "
        for i in range(len(keys)):                      # Add all update arguments to the string
            commandStr += "{} = %s,".format(keys[i])
        commandStr = commandStr[:-1].replace(";", "")   # To avoid SQL injections and remove last comma
        commandStr += " WHERE userid = %s AND typeid = %s AND rdatetime = %s;" 

        super()._cur.execute(commandStr, values)


    @classmethod
    def delete(cls, record_id: list):
        """ Takes in a list of ints. Deletes row with those id's from the database. Returns nothing """
        super()._cur.execute("DELETE FROM users WHERE userid = %s AND typeid = %s AND rdatetime = %s;", (record_id[0], record_id[1], record_id[2]))