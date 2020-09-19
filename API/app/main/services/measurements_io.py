from main.services.abc_table import AbcTable

class Measurementsio(AbcTable):
    @classmethod
    def get(cls, measurement_id):
        """ Takes in an int. Returns row from habits with set id or all rows if id=None """
        if measurement_id:
            super()._cur.execute("SELECT * FROM measurements WHERE measurementid = %s;", (measurement_id,))
        else:
            super()._cur.execute("SELECT * FROM measurements;")
        return super()._cur.fetchall()

    @classmethod
    def post(cls, data):
        pass

    @classmethod
    def put(cls, measurement_id, data):
        pass

    @classmethod
    def delete(cls, measurement_id):
        pass