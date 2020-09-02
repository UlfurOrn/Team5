from abctable import *

class Usersio(Abctable):
    @classmethod
    def get(cls, id):
        super()._cur.execute("SELECT * FROM users;")  # Example of a command
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
    Usersio.get(0)