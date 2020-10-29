from main.repositories.abc_table import AbcTable
from main.util.mappers.habitmapper import HabitMapper
from psycopg2.extensions import AsIs  # Used to remove '' from SQL strings I insert


class HabitsIO(AbcTable):
    """
        An input-output class for the habits table in the Habit tracker database.
        Contains methods for each CRUD operation [GET, POST, PUT, DELETE]
    """
    table = "habits"
    table_key="habitid"

    @classmethod
    def get(cls, habit_id=None, user_id=None):
        """ Takes in an int. Returns row from habits with set id or all rows if id=None as list of Habit objects"""
        cls.test_connection()
        if habit_id:
            super()._cur.execute("SELECT * FROM habits WHERE habitid = %s;", (habit_id,))
        elif user_id:
            super()._cur.execute("SELECT * FROM habits WHERE userid = %s", (user_id,))
        else:
            super()._cur.execute("SELECT * FROM habits;")

        habits_list = []
        try:
            for habit_info in super()._cur.fetchall():
                habit = HabitMapper(*habit_info)
                habits_list.append(habit)

        return habits_list
