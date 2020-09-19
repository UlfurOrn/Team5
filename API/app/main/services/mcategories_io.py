from main.services.abc_table import AbcTable

class Mcategoriesio(AbcTable):
    @classmethod
    def get(cls, mcategory_id):
        """ Takes in an int. Returns row from habits with set id or all rows if id=None """
        if mcategory_id:
            super()._cur.execute("SELECT * FROM mcategories WHERE mcategoryid = %s;", (mcategory_id,))
        else:
            super()._cur.execute("SELECT * FROM mcategories;")
        return super()._cur.fetchall()

    @classmethod
    def post(cls, data):
        pass

    @classmethod
    def put(cls, mcategory_id, data):
        pass

    @classmethod
    def delete(cls, habitmcategory_id):
        pass