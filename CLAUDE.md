# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal library management system for home use. Users can check out books, place holds, and view their history. Users should only have access to their own accounts. PostgreSQL database stores the catalog, user checkouts, and holds.

## Commands

### Run locally (dev server with hot reload)
```
uvicorn src.main:app --reload
```

### Run with Docker Compose (app + Postgres)
```
docker-compose up
```

### Install dependencies
```
pip install -r requirements.txt
```

## Architecture

- **FastAPI app** — entry point is `src/main.py` (`app = FastAPI()`)
- **Domain models** — `src/book.py` (Book, BookStatus enum), `src/user.py` (User with Pydantic BaseModel)
- **Database** — PostgreSQL via SQLModel (`src/database.py`), config via pydantic-settings (`src/config.py`)
- **Config** — `src/config.py` reads DB settings from env vars: `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`

The project is early-stage. Domain models are not yet wired into SQLModel tables, and routes beyond root/ping are not yet implemented. `src/user.py` imports from a deleted `catalog.py` that needs resolving.

## Key Design Decisions

- Users must only access their own account data (checkouts, holds, history)
- PostgreSQL 16 for persistence (via Docker Compose)
- SQLModel for ORM layer, pydantic-settings for configuration
- Python 3.12, virtualenv at `.venv/`
