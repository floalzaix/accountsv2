FROM python:3.12.10-slim AS backend-builder

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry && \
poetry config virtualenvs.in-project true && \
poetry install --no-root

FROM python:3.12.10-slim AS backend

WORKDIR /app

RUN apt update && \
    apt install -y build-essential gcc g++ make libffi-dev libssl-dev && \
    apt install -y curl && \
    pip install poetry && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

COPY --from=backend-builder /app/.venv /app/.venv

COPY . .

RUN useradd -m backuser && \
    chown -R backuser:backuser /app && \
    chmod -R 755 /app

USER backuser

EXPOSE 5050

CMD ["poetry", "run", "uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "5050"]