@echo off
poetry run alembic upgrade head
poetry run uvicorn main:app --reload --port 5050