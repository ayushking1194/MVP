FROM python:3.10-slim

WORKDIR /app

# system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# copy poetry files
COPY pyproject.toml /app/

RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# copy app
COPY src/ /app/
COPY config/ /app/config/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]