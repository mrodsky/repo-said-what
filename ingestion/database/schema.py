import sqlite3

def create_messages_table(conn: sqlite3.Connection):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id TEXT PRIMARY KEY,
            timestamp TEXT NOT NULL,
            content TEXT,
            attachments TEXT
        )
    """)