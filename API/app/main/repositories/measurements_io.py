from main.repositories.abc_table import AbcTable
from main.util.mappers.measurement import Measurement

class Measurementsio(AbcTable):
    @classmethod
    def get(cls, measurement_id):
        """ Takes in an int. Returns row from habits with set id or all rows if id=None """
        if measurement_id:
            super()._cur.execute("SELECT * FROM measurements WHERE measurementid = %s;", (measurement_id,))
        else:
            super()._cur.execute("SELECT * FROM measurements;")
        measurements_list = []
        for measurement in super()._cur.fetchall():
            measurements_list.append(Measurement(*measurement))
        return measurements_list

    @classmethod
    def post(cls, data):
        pass

    @classmethod
    def put(cls, measurement_id, data):
        pass

    @classmethod
    def delete(cls, measurement_id):
        pass