import os
import orjson
from pathlib import Path
from pprint import pp
from datetime import datetime
from discord_reader import find_message_files, find_channel_files, find_guild_files, load_messages
from parser import parse_message
from database.connection import create_database, initialize_database
from database.message_repository import save_message
from database.schema import create_messages_table

def main():
    
    print(f"{datetime.now()} \t Start \t {__file__} ")
    ingest_messages()
 
    print(f"{datetime.now()} \t End \t {__file__} ")

#############################################################################################

def ingest_messages():
    base_path = Path(r"E:\\Projects\\repo-said-what\\data\\DiscordMessages")
    db_file_path = Path(r"E:\\Projects\\repo-said-what\\data\\discord.db")

    #now for each message file, load the messages, parse them, and save them to the database
    total_cnt, commit_cnt = 0, 0

    try:
        #first create the DB 
        with create_database(db_file_path) as conn:
            initialize_database(conn)

            total_json_messages = 0
            total_parsed_messages = 0
            total_saved_messages = 0

            for file_path in find_message_files(base_path):
                messages = load_messages(file_path)

                print(f"{file_path.name}: {len(messages)} messages loaded")

                total_json_messages += len(messages)

                for msg in messages:
                    message = parse_message(msg)
                    total_parsed_messages += 1

                    save_message(conn, message)
                    total_saved_messages += 1
                    commit_cnt += 1
                    total_cnt += 1
                    if commit_cnt >= 1000:
                        conn.commit()
                        commit_cnt = 0
        
            conn.commit()  # Commit any remaining messages
            print(f"JSON messages: {total_json_messages}")
            print(f"Parsed messages: {total_parsed_messages}")
            print(f"Saved messages: {total_saved_messages}")

        print(f"{datetime.now()} \t Inserted {total_cnt} messages")

    except Exception as e:
        print(f"Error initializing database: {e}")
        conn.close()
        return

def walkfolders():
    # This function will walk through folders and perform some operations
    for root, dirs, files in os.walk("E:\\Projects\\repo-said-what\\data\\DiscordMessages"):
        json_files = [f for f in files if f.endswith('.json')]
        if json_files:
            if "messages.json" in json_files:
                file_path = os.path.join(root, "messages.json")
                with open(file_path, 'rb') as f:
                    data = orjson.loads(f.read())
                    print(f"\nFolder: {root}")
                    print(f"File: messages.json")
                    print(f"Data: {data}")

def walkmessages():
    base = r"E:\Projects\repo-said-what\data\DiscordMessages"

    for root, dirs, files in os.walk(base):
        if "messages.json" in files:
            print(f"Found messages: {os.path.join(root, 'messages.json')}")

def walkchannel():
    base = r"E:\Projects\repo-said-what\data\DiscordMessages"

    for root, dirs, files in os.walk(base):
        if "channel.json" in files:
            print(f"Found channel: {os.path.join(root, 'channel.json')}")

def walkguild():
    base = r"E:\Projects\repo-said-what\data\DiscordMessages"

    for root, dirs, files in os.walk(base):
        if "guild.json" in files:
            print(f"Found guild: {os.path.join(root, 'guild.json')}")


if __name__ == "__main__":
    main()