FROM python:3.12.10-slim AS backend-builder

WORKDIR /app

# For psycopg2
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        python3-dev && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock ./

RUN pip install poetry && \
poetry config virtualenvs.in-project true && \
poetry install --no-root

FROM python:3.12.10-slim AS backend

# For psycopg2
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libpq5 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY --from=backend-builder /app/.venv /app/.venv

COPY . .

RUN useradd -m backuser && \
    chown -R backuser:backuser /app && \
    chmod -R 755 /app && \
    pip install poetry

USER backuser

EXPOSE 5050

CMD ["sh", "-c", "poetry run alembic upgrade head && poetry run uvicorn main:app --host 0.0.0.0 --port 5050 --proxy-headers --forwarded-allow-ips='*'"]

# accounts-v2
