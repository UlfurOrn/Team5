from abctable import *

class Recordsio(Abctable):
    @classmethod
    def get(cls, id):
        if id != []:
            super()._cur.execute("SELECT * FROM records WHERE userid = %s AND typeid = %s AND rdatetime = %s;", (id[0], id[1], id[2]))
        else:
            super()._cur.execute("SELECT * FROM records;")
        return super()._cur.fetchall()


    @classmethod
    def post(cls, data):
        userid, typeid, rdatetime, ammount = data["UserId"], data["TypeId"], data["RDateTime"], data["Amount"]
        super()._cur.execute("INSERT INTO records VALUES (%s, %s, %s, %s)", (userid, typeid, rdatetime, ammount))


    @classmethod
    def put(cls, id, data):
        values = [val for val in data.values()] # Get all keys from the input dict
        keys = [key for key in data.keys()]     # Get all values from the input dict
        values.extend(id)

        commandStr = "UPDATE records SET "
        for i in range(len(keys)):                      # Add all updates to string
            commandStr += "{} = %s,".format(keys[i])
        commandStr = commandStr[:-1].replace(";", "")   # To avoid SQL injections and remove last comma
        commandStr += " WHERE userid = %s AND typeid = %s AND rdatetime = %s;" 

        super()._cur.execute(commandStr, values)


    @classmethod
    def delete(cls, id):
        super()._cur.execute("DELETE * FROM users WHERE userid = %s AND typeid = %s AND rdatetime = %s;", (id[0], id[1], id[2]))





if __name__ == "__main__":
    print(Recordsio.get([1, 1, '2020-09-03 10:05:26']))
    Recordsio.put([1, 1, '2020-09-03 10:05:26'], {"ammount": "1000"})
    print(Recordsio.get([1, 1, '2020-09-03 10:05:26']))
    print (Recordsio.get([]))