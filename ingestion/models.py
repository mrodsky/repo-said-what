from dataclasses import dataclass
from datetime import datetime

@dataclass(slots=True)
class Message:
    id: str
    timestamp: datetime
    content: str
    attachments: str

@dataclass(slots=True)
class Channel:
    id: str
    type: str
    messages: list[Message]