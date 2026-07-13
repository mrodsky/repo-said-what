import sqlite3
from models import Message

def save_message(conn: sqlite3.Connection, message: Message):
    conn.execute(
        '''
        INSERT OR REPLACE 
        INTO messages 
        (
            id,
            timestamp,
            content,
            attachments
        )
        VALUES (?, ?, ?, ?)
        ''',
        (
            message.id,
            message.timestamp.isoformat(),
            message.content,
            message.attachments
        ),
    )