import psycopg2
from psycopg2 import OperationalError
from psycopg2 import pool

USER ='kramos'
PASSWORD ='1102359KeRa%'

def test_connection():
    try:

        db_pool = pool.SimpleConnectionPool(
            1, 4,
            host="localhost",
            database="PostgresI",
            user=USER,
            password=PASSWORD
        )

        # Get connection from pool
        connection = db_pool.getconn()

        # Create cursor
        cursor = connection.cursor()

        return cursor

    except OperationalError as e:
        print("Connection failed")
        print(e)


if __name__ == "__main__":
    cursor = test_connection()

    if cursor:
        cursor.execute("SELECT current_database();")
        print(cursor.fetchone())