from abctable import *

class Usersio(Abctable):
    @classmethod
    def get(cls, id):
        if id:
            super()._cur.execute("SELECT * FROM users WHERE userid = %s;", (id,))
        else:
            super()._cur.execute("SELECT * FROM users;")
        return super()._cur.fetchall()

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