from main.repositories.abc_table import AbcTable
from main.util.mappers.categorymapper import CategoryMapper


class McategoriesIO(AbcTable):
    @classmethod
    def get(cls, mcategory_id=None):
        """ Takes in an int. Returns row from habits with set id or all rows if id=None """
        cls.test_connection()
        if mcategory_id:
            super()._cur.execute("SELECT * FROM mcategories WHERE mcategoryid = %s;", (mcategory_id,))
        else:
            super()._cur.execute("SELECT * FROM mcategories;")

        category_list = []
        try:
            for category_info in super()._cur.fetchall():
                category = CategoryMapper(*category_info)
                category_list.append(category)
        except:
            pass
        
        return category_list
