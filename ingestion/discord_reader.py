import os
from pathlib import Path; 
import orjson
from parser import parse_message
from models import Message

def find_message_files(base_path):
    base_path = Path(base_path)
    for file in base_path.rglob("messages.json"):
        yield file

def find_channel_files(base_path):
    base_path = Path(base_path)
    for file in base_path.rglob("channel.json"):
        yield file

def find_guild_files(base_path):
    base_path = Path(base_path)
    for file in base_path.rglob("guild.json"):
        yield file

def load_messages(message_file: Path) -> list[dict]:
    with message_file.open("rb") as f:
        return orjson.loads(f.read())
