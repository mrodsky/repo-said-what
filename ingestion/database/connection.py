from contextlib import contextmanager
import sqlite3
import pathlib
from database.schema import create_messages_table

@contextmanager
def create_database(db_file_path: pathlib.Path):
    try:
        conn = sqlite3.connect(db_file_path)
        yield conn
    finally:
        conn.close()


def initialize_database(conn: sqlite3.Connection):
    create_messages_table(conn)
    conn.commit()   