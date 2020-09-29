from main.repositories.abc_table import AbcTable
from main.util.mappers.record import Record
from psycopg2.extensions import AsIs  # Used to remove '' from SQL strings I insert


class Recordsio(AbcTable):
    """
        An input-output class for the records table in the Habit tracker database.
        Contains methods for each CRUD operation [GET, POST, PUT, DELETE]
    """

    @classmethod
    def get(cls, record_id: int):
        """ Takes in an int. Returns row from records with set id or all rows if id=None as a list of Record objects """
        if record_id:
            super()._cur.execute("SELECT * FROM records WHERE recordid = %s;", (record_id,))
        else:
            super()._cur.execute("SELECT * FROM records;")
        records_list = []
        for record in super()._cur.fetchall():
            records_list.append(Record(*record))
        return records_list

    @classmethod
    def post(cls, data: dict):
        """
        Takes in a Record object and saves it to the database.
        Returns nothing
        """
        record_tuple = data.to_sql_insert()
        super()._cur.execute("INSERT INTO records %s VALUES %s;", (AsIs(record_tuple[0]), AsIs(record_tuple[1])))

    @classmethod
    def put(cls, record_id: int, data: dict):
        """
        Takes in an int and a Record object with changes and updates those
        columns in the database. Returns nothing
        """
        record_str = data.to_sql_update()
        super()._cur.execute("UPDATE records SET %s WHERE recordid = %s", (AsIs(record_str), record_id))

    @classmethod
    def delete(cls, record_id: int):
        """
        Takes in a list of ints. Deletes row with those id's from the database.
        Returns nothing
        """
        super()._cur.execute("DELETE FROM records WHERE recordid = %s;", (record_id,))
