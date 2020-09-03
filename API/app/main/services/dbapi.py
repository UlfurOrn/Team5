from usersio import Usersio
from recordsio import Recordsio
from typesio import Typesio

class DBapi():
    methods = ["GET", "POST", "PUT", "DELETE"]
    @classmethod
    def users(cls, method: str, id: int=None, data=None):
        if method == cls.methods[0]:
            return Usersio.get(id)

        elif method == cls.methods[1]:
            if data:
                Usersio.post(data)
            else:
                raise Exception("Missing data")

        elif method == cls.methods[2]:
            if id:
                if data:
                    Usersio.put(id, data)
                else:
                    raise Exception("Missing data")
            else:
                raise Exception("Missing id")

        elif method == cls.methods[3]:
            if id:
                Usersio.delete(id)
            else:
                raise Exception("Missing id")

        else:
            raise Exception("Method not in list of approved methods: {}".format(cls.methods))

    @classmethod
    def types(cls, method: str, id: int=None, data=None):
        if method == cls.methods[0]:
            return Typesio.get(id)

        elif method == cls.methods[1]:
            if data:
                Typesio.post(data)
            else:
                raise Exception("Missing data")

        elif method == cls.methods[2]:
            if id:
                if data:
                    Typesio.put(id, data)
                else:
                    raise Exception("Missing data")
            else:
                raise Exception("Missing id")

        elif method == cls.methods[3]:
            if id:
                Typesio.delete(id)
            else:
                raise Exception("Missing id")

        else:
            raise Exception("Method not in list of approved methods: {}".format(cls.methods))

    @classmethod
    def records(cls, method: str, ids: list=None, data=None):
        if method == cls.methods[0]:
            return Recordsio.get(id)

        elif method == cls.methods[1]:
            if data:
                Recordsio.post(data)
            else:
                raise Exception("Missing data")

        elif method == cls.methods[2]:
            if id:
                if data:
                    Recordsio.put(id, data)
                else:
                    raise Exception("Missing data")
            else:
                raise Exception("Missing id")

        elif method == cls.methods[3]:
            if id:
                Recordsio.delete(id)
            else:
                raise Exception("Missing id")

        else:
            raise Exception("Method not in list of approved methods: {}".format(cls.methods))


if __name__ == "__main__":
    DBapi.users("GET")
    print(DBapi.types("GET", 1))
    DBapi.records("GET")