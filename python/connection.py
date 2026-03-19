import psycopg2
from psycopg2 import OperationalError
from psycopg2 import pool
import Postgres as pg




def connection(USER, PASSWORD, db_to_use):
    return ( pg.connection(USER, PASSWORD, db_to_use))



