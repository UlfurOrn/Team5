from main.repositories.abc_table import AbcTable
from main.util.mappers.recordmapper import RecordMapper
from psycopg2.extensions import AsIs  # Used to remove '' from SQL strings I insert


class RecordsIO(AbcTable):
    """
        An input-output class for the records table in the Habit tracker database.
        Contains methods for each CRUD operation [GET, POST, PUT, DELETE]
    """
    table = "records"
    table_key = "recordid"

    @classmethod
    def get(cls, record_id=None, habit_id=None, user_id=None, date_start=None, date_end=None):
        """ Takes in an int. Returns row from records with set id or all rows if id=None as a list of Record objects """
        cls.test_connection()
        if user_id and date_start and date_end:
            super()._cur.execute("SELECT * FROM records WHERE userid = %s AND rdate BETWEEN %s AND %s;", (user_id, date_start, date_end))
        elif record_id:
            super()._cur.execute("SELECT * FROM records WHERE recordid = %s;", (record_id,))
        elif habit_id:
            super()._cur.execute("SELECT * FROM records WHERE habitid = %s;", (habit_id,))
        elif user_id:
            super()._cur.execute("SELECT * FROM records WHERE userid = %s;", (user_id,))
        else:
            super()._cur.execute("SELECT * FROM records;")

        records_list = []
        for record_info in super()._cur.fetchall():
            record = RecordMapper(*record_info)
            records_list.append(record)

        return records_list