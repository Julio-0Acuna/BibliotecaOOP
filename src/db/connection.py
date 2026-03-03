import mysql.connector
from mysql.connector import pooling
from src.config import DB_CONFIG

_pool = pooling.MySQLConnectionPool(
    pool_name="biblioteca_pool",
    pool_size=5,
    **DB_CONFIG
)

def get_conn():
    return _pool.get_connection()