import psycopg2
from psycopg2 import OperationalError


def test_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            port=5432,
            database="postgres",      # change if needed
            user="postgres",          # change if needed
            password="F1shnR0d"  # change if needed
        )

        cursor = connection.cursor()

        # Run a simple query to verify the DB responds
        cursor.execute("SELECT * from papasitos.table_one;")

        result = cursor.fetchone()

        print("Connection successful")
        print("PostgreSQL version:")
        print(result[0])

        cursor.close()
        connection.close()

        print("Connection closed")

    except OperationalError as e:
        print("Connection failed")
        print(e)


if __name__ == "__main__":
    test_connection()