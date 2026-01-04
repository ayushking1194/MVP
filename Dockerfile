FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock /app/

# Copy application code
COPY src/ /app/src/
COPY config/ /app/config/

RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi


# switch working directory to src
WORKDIR /app/src

EXPOSE 8000

# Run main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]