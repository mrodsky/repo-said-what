from datetime import datetime

from parser import parse_message

def test_parse_message():
    raw_message = {
        "ID": 123,
        "Timestamp": "2023-06-01 12:34:56",
        "Contents": "Hello, world!",
        "Attachments": ["file1.txt", "file2.jpg"]
    }

    message = parse_message(raw_message)

    assert message.id == "123"
    assert message.timestamp == datetime(2023, 6, 1, 12, 34, 56)
    assert message.content == "Hello, world!"
    assert message.attachments == ["file1.txt", "file2.jpg"]