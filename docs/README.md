# Repo Said What

## Overview

Repo Said What is a personal Discord archive application that ingests exported Discord message history and provides a searchable web interface.

The project is intended to be both a useful personal archive and a learning project focused on modern Python backend development, React, Docker, and AWS deployment.

---

# Goals

* Import Discord export data into a normalized database
* Provide fast full-text message search
* Browse servers, channels, and conversations
* Support authenticated users
* Deploy using AWS Fargate
* Learn modern Python backend development with FastAPI

---

# Planned Technology Stack

## Backend

* Python
* FastAPI
* SQLite (initially)
* SQLAlchemy / SQLModel (TBD)
* JWT Authentication

## Frontend

* React
* REST API

## Infrastructure

* Docker
* AWS Fargate
* SQLite (initial version)

Future versions may migrate to PostgreSQL if application requirements outgrow SQLite.

---

# Repository Structure

```text
repo-said-what/

backend/
    FastAPI application

frontend/
    React application

ingestion/
    Discord import pipeline

data/
    Local SQLite database
    Discord exports (gitignored)

docs/
    Project documentation
```

---

# Development Roadmap

## Phase 1 — Data Ingestion

### Objectives

* Read Discord export
* Parse every server
* Parse every channel
* Parse every message
* Create normalized SQLite database

### Initial Tables

* Servers
* Channels
* Messages

The first milestone is simply proving that every exported message can be imported successfully.

---

## Phase 2 — Backend API

Build a FastAPI backend capable of:

* Listing servers
* Listing channels
* Viewing messages
* Searching messages

Authentication is intentionally postponed until the API is functional.

---

## Phase 3 — Frontend

Build a React frontend that consumes the REST API.

Initial functionality:

* Login
* Server browser
* Channel browser
* Message viewer
* Search

---

## Phase 4 — Authentication

Implement user authentication using:

* Password hashing
* JWT tokens
* User roles (Admin / Viewer)

The ingestion process is considered an administrative operation and will not use a normal user account.

---

## Phase 5 — Deployment

Containerize the backend and frontend.

Deploy to AWS Fargate.

---

# Discord Export Structure

The Discord export currently follows this layout:

```text
DiscordMessages/

Messages/
    c<channel id>/
        channel.json
        messages.json

Servers/
    <server id>/
        guild.json
        audit-log.json
```

The importer will recursively discover all channels, read the associated metadata, and import all messages into the database.

---

# Initial Milestone

The first completed version of the project should be able to:

* Read every `channel.json`
* Read every `messages.json`
* Build a SQLite database
* Print import statistics
* Verify that all messages were imported successfully

No frontend or API work should begin until the ingestion pipeline is complete and the database schema has stabilized.

---

# Future Features

* Full-text search
* Attachments
* Reactions
* Threads
* Message editing history
* User profiles
* Advanced search filters
* Incremental imports
* PostgreSQL migration (if required)
