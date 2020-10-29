from main.repositories.abc_table import AbcTable
from main.util.mappers.measurementmapper import MeasurementMapper


class MeasurementsIO(AbcTable):
    @classmethod
    def get(cls, measurement_id=None):
        """ Takes in an int. Returns row from habits with set id or all rows if id=None """
        cls.test_connection()
        if measurement_id:
            super()._cur.execute("SELECT * FROM measurements WHERE measurementid = %s;", (measurement_id,))
        else:
            super()._cur.execute("SELECT * FROM measurements;")

        measurements_list = []
        try:
            for measurement_info in super()._cur.fetchall():
                measurement = MeasurementMapper(*measurement_info)
                measurements_list.append(measurement)
        except:
            pass
        
        return measurements_list