from django.db import connections
from django.db.utils import OperationalError


def check_database_connection():
    try:
        # Attempt to access the database to check the connection
        connections['default'].cursor()
        return True  # Connection is successful
    except OperationalError:
        return False  # Connection failed


# Call the function to check the connection
if check_database_connection():
    print("Database connection is established.")
else:
    print("Database connection is not established.")
