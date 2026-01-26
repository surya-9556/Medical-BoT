# Base image
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY . .

# Install uv and dependencies
RUN python -m ensurepip --upgrade \
    && python -m pip install --no-cache-dir uv \
    && uv pip install --system --no-cache-dir

EXPOSE 5000

CMD ["uv", "run", "app/application:app", "--host", "0.0.0.0", "--port", "5000"]
