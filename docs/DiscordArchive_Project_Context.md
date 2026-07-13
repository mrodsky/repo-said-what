# Discord Archive Project -- Context Summary

## Goal

Build a local Discord archive/search application.

Current focus is the **ingestion** stage: 1. Discover exported Discord
JSON files. 2. Parse them. 3. Store them in SQLite. 4. Later expose them
through a FastAPI backend and React frontend.

------------------------------------------------------------------------

## Project Structure

``` text
repo-said-what/
├── ingestion/
│   ├── main.py
│   ├── discord_reader.py
│   ├── parser.py
│   ├── models/
│   │   └── message.py
│   ├── database/
│   │   ├── connection.py
│   │   ├── schema.py
│   │   └── message_repository.py
│   └── tests/
│       ├── Fixtures/
│       └── test_discord_reader.py
└── data/
    ├── DiscordMessages/
    └── discord.db
```

------------------------------------------------------------------------

## Tooling

-   Python managed with **uv**
-   Virtual environment: `ingestion/.venv`
-   Packages:
    -   orjson
    -   pytest
-   SQLite via Python `sqlite3` (built-in)

Useful commands:

``` bash
uv add orjson
uv add --dev pytest
uv run python main.py
uv run pytest
```

------------------------------------------------------------------------

## Current Pipeline

`find_message_files()` recursively finds every `messages.json`.

`load_messages()` reads JSON using:

``` python
orjson.loads(...)
```

Each file returns:

``` python
list[dict]
```

Each dict represents one Discord message.

`parse_message()` converts raw dictionaries into a `Message` dataclass.

Each parsed message is inserted through `save_message()`.

------------------------------------------------------------------------

## Database

Current database:

    data/discord.db

Current table:

``` sql
messages
--------
id TEXT PRIMARY KEY
timestamp TEXT
content TEXT
attachments TEXT
```

Repository pattern:

-   connection.py
-   schema.py
-   message_repository.py

------------------------------------------------------------------------

## Database Initialization

`create_database()` returns a sqlite connection.

`initialize_database()` creates schema.

Using:

``` python
with create_database(db_path) as conn:
```

The context manager closes the connection automatically.

------------------------------------------------------------------------

## Tests

Using pytest.

Current tests cover:

-   recursive discovery of message files

Fixtures live under:

    tests/Fixtures/

Future tests should cover:

-   parser
-   repository
-   end-to-end ingestion

------------------------------------------------------------------------

## Current Status

Ingestion is working.

Current database contains:

-   91 `messages.json` files
-   112,694 messages successfully imported

Verified using:

``` bash
sqlite3 data/discord.db "SELECT COUNT(*) FROM messages;"
```

------------------------------------------------------------------------

## Lessons Learned

-   `yield` creates generators/context managers.
-   `return` immediately exits a function.
-   `list(generator)` eagerly evaluates a generator.
-   `orjson.loads()` returns normal Python objects.

------------------------------------------------------------------------

## Next Planned Work

1.  Add Channels table.
2.  Add Guilds table.
3.  Store `channel_id` on messages.
4.  Store guild relationships.
5.  Add author/user tables.
6.  Improve schema with indexes.
7.  Build FastAPI API.
8.  Build React frontend.

------------------------------------------------------------------------

## Known Issues

The VS Code SQLite extension (`alexcvzz.vscode-sqlite` v0.14.1) fails to
open the database with:

    no such column: "table"

The SQLite CLI works correctly, so the database itself is healthy.

Current recommendation is to use:

``` bash
sqlite3 data/discord.db
```

for inspection until a different VS Code extension is chosen.

------------------------------------------------------------------------

## Architectural Decisions

-   Keep parsing separate from persistence.
-   Keep database access in repository modules.
-   Use dataclasses for domain models.
-   Commit SQLite transactions in batches (\~1000 rows).
-   Favor pathlib over os.path for new code.
-   Continue writing unit tests as features are added.
