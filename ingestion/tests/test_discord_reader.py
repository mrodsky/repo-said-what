from pathlib import Path
from discord_reader import find_message_files, find_channel_files, find_guild_files

def test_find_message_files():
    #arrange
    base_path = Path("E:\\Projects\\repo-said-what\\ingestion\\tests\\Fixtures\\DiscordMessages")
    #act
    message_files = list(find_message_files(base_path))
    #assert
    expected_file = Path(
        base_path /
        "cq155dq4wc89cqc1qc56c1q" /
        "messages.json"
    )
    assert message_files == [expected_file]

def test_find_message_files_no_results():
    #arrange
    base_path = Path("E:\\Projects\\repo-said-what\\ingestion\\tests\\Fixtures\\DiscordMessages\\no_messages")
    #act
    message_files = list(find_message_files(base_path))
    #assert
    expected_file = list()
    assert message_files == expected_file



def test_find_guild_files():
    #arrange
    base_path = Path("E:\\Projects\\repo-said-what\\ingestion\\tests\\Fixtures\\DiscordMessages")
    #act
    guild_files = list(find_guild_files(base_path))
    #assert
    expected_file = Path(
        base_path /
        "cq155dq4wc89cqc1qc56c1q" /
        "guild.json"
    )
    assert guild_files == [expected_file]

def test_find_guild_files_no_results():
    #arrange
    base_path = Path("E:\\Projects\\repo-said-what\\ingestion\\tests\\Fixtures\\DiscordMessages\\no_guild")
    #act
    guild_files = list(find_guild_files(base_path))
    #assert
    expected_file = list()
    assert guild_files == expected_file


def test_find_channel_files():
    #arrange
    base_path = Path("E:\\Projects\\repo-said-what\\ingestion\\tests\\Fixtures\\DiscordMessages")
    #act
    channel_files = list(find_channel_files(base_path))
    #assert
    expected_file = Path(
        base_path /
        "cq155dq4wc89cqc1qc56c1q" /
        "channel.json"
    )
    assert channel_files == [expected_file]

    
def test_find_channel_files_no_results():
    #arrange
    base_path = Path("E:\\Projects\\repo-said-what\\ingestion\\tests\\Fixtures\\DiscordMessages\\no_channel")
    #act
    channel_files = list(find_channel_files(base_path))
    #assert
    expected_file = list()
    assert channel_files == expected_file