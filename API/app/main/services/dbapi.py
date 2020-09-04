from usersio import Usersio
from recordsio import Recordsio
from typesio import Typesio

class DBapi():
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    
    @classmethod
    def users(cls, method: str, id: int=None, data=None):
        if method == cls.GET:
            return Usersio.get(id)

        elif method == cls.POST:
            if data:
                Usersio.post(data)
            else:
                raise Exception("Missing data")

        elif method == cls.PUT:
            if id:
                if data:
                    Usersio.put(id, data)
                else:
                    raise Exception("Missing data")
            else:
                raise Exception("Missing id")

        elif method == cls.DELETE:
            if id:
                Usersio.delete(id)
            else:
                raise Exception("Missing id")

        else:
            raise Exception("Method not in list of approved methods: {}".format(cls.methods))

    @classmethod
    def types(cls, method: str, id: int=None, data=None):
        if method == cls.GET:
            return Typesio.get(id)

        elif method == cls.POST:
            if data:
                Typesio.post(data)
            else:
                raise Exception("Missing data")

        elif method == cls.PUT:
            if id:
                if data:
                    Typesio.put(id, data)
                else:
                    raise Exception("Missing data")
            else:
                raise Exception("Missing id")

        elif method == cls.DELETE:
            if id:
                Typesio.delete(id)
            else:
                raise Exception("Missing id")

        else:
            raise Exception("Method not in list of approved methods: {}".format(cls.methods))

    @classmethod
    def records(cls, method: str, ids: list=[], data=None):
        if method == cls.GET:
            return Recordsio.get(ids)

        elif method == cls.POST:
            if data:
                Recordsio.post(data)
            else:
                raise Exception("Missing data")

        elif method == cls.PUT:
            if id:
                if data:
                    Recordsio.put(ids, data)
                else:
                    raise Exception("Missing data")
            else:
                raise Exception("Missing id")

        elif method == cls.DELETE:
            if id:
                Recordsio.delete(ids)
            else:
                raise Exception("Missing id")

        else:
            raise Exception("Method not in list of approved methods: {}".format(cls.methods))


if __name__ == "__main__":
    """
    users = DBapi.users("GET")
    types = DBapi.types("GET", 1)
    print (users[0]["userid"])
    print(DBapi.records("GET"))
    print(DBapi.records("GET", [1, 1, '2020-09-03 10:05:26']))
    """