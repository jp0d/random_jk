import time
import duckdb

def connect(db_file = "local.db"):
    conn = duckdb.connect(db_file)
    cursor = conn.cursor()
    return conn

def create_insert_db(db_conn, table_name, key_list, data):
    columns = str()
    for s in key_list:
        columns = columns + s + ' varchar, '

    db_conn.execute(f'CREATE TABLE  IF NOT EXISTS {table_name} ({columns[:-2]}) ')
    db_conn.execute(f'INSERT INTO {table_name} SELECT * FROM {data}')
    db_conn.commit()
