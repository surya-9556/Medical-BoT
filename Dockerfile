# Base image
FROM python:3.13-slim

# Environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Allow dynamic UV version
ARG UV_VERSION=latest

# Install uv and dependencies from pyproject.toml
RUN python -m ensurepip --upgrade \
    && python -m pip install --no-cache-dir "uv==$UV_VERSION" \
    && uv install --no-cache-dir

# Expose port
EXPOSE 5000

# Run your application with uv
CMD ["uv", "run", "app/application:app", "--host", "0.0.0.0", "--port", "5000"]
