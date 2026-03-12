import psycopg2
from psycopg2 import OperationalError

password="Enter Information"

def test_connection():
    try:
        connection = psycopg2.connect(
            host="34.174.195.206",
            port=5432,
            database="PostgresI",      # change if needed
            user="postgres",          # change if needed
            password=password  # change if needed
        )

        cursor = connection.cursor()

        # Run a simple query to verify the DB responds
        # Running tests
        cursor.execute("select * from postgresI.papasitos.table_one;")

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