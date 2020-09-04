from abctable import *

class Typesio(Abctable):
    @classmethod
    def get(cls, id):
        if id:
            super()._cur.execute("SELECT * FROM types WHERE typeid = %s;", (id,))
        else:
            super()._cur.execute("SELECT * FROM types;")
        return super()._cur.fetchall()

    @classmethod
    def post(cls, data):
        pass

    @classmethod
    def put(cls, id, data):
        pass

    @classmethod
    def delete(cls, id):
        super()._cur.execute("DELETE * FROM types WHERE typeid = %s;", (id,))

if __name__ == "__main__":
    Typesio.get(0)