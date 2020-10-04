class DBapiCreator():
    """
        A class that satisfies the Dependency Injection. Takes in io classes and allows
        the creation of a DBapi from those io classes. Makes it easy to swap out different
        databases without changing other code
    """
    def __init__(self, usersio, habitsio, recordsio, mcategoriesio, measurementsio):
        self.users = usersio
        self.habits = habitsio
        self.records = recordsio
        self.mcategories = mcategoriesio
        self.measurements = measurementsio