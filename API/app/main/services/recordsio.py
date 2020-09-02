from abctable import *

class Recordsio(Abctable):
    @classmethod
    def get(cls, id):
        super()._cur.execute("SELECT * FROM records;")  # Example of a command
        print (super()._cur.fetchall())

    @classmethod
    def post(cls, data):
        pass

    @classmethod
    def put(cls, id, data):
        pass

    @classmethod
    def delete(cls, id):
        pass

if __name__ == "__main__":
    Recordsio.get(0)