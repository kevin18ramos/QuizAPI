import psycopg2
from psycopg2 import OperationalError

USER =readonly_test
PASSWORD ='t3st123'

def test_connection():
    try:
        connection = psycopg2.connect(
            host="34.174.195.206",
            port=5432,
            database="PostgresI",      # change if needed
            user=USER,          # change if needed
            password=PASSWORD  # change if needed
        )

        cursor = connection.cursor()

        # Run a simple query to verify the DB responds
        # Running tests
        x = cursor.execute("select * from papasitos.table_one;")

        result = cursor.fetchone()

        print("Connection successful")
        print("PostgreSQL version:")
        print('result: ',result)

        cursor.close()
        connection.close()

        print("Connection closed")

    except OperationalError as e:
        print("Connection failed")
        print(e)


if __name__ == "__main__":
    test_connection()