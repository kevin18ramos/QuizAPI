import psycopg2
from psycopg2 import OperationalError
from psycopg2 import pool
import gcc_postgres as pg




def connection(caller_file=__file__):
    return ( pg.d_cn(caller_file))



