from main.repositories.users_io import UsersIO
from main.repositories.records_io import RecordsIO
from main.repositories.habits_io import HabitsIO
from main.repositories.measurements_io import MeasurementsIO
from main.repositories.mcategories_io import McategoriesIO

from main.services.db_api_creator import DBapiCreator

# Create a new DBapi using our Postgresql IO classes
DBapi = DBapiCreator(UsersIO, HabitsIO, RecordsIO, McategoriesIO, MeasurementsIO)