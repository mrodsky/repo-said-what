from datetime import datetime
from models import Message


def parse_message(raw: dict) -> Message:
    return Message(
        id=str(raw["ID"]),
        timestamp=datetime.strptime(
            raw["Timestamp"],
            "%Y-%m-%d %H:%M:%S"
        ),
        content=raw["Contents"],
        attachments=raw["Attachments"],
    )