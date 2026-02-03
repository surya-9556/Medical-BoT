#!/usr/bin/env bash
set -e

echo "Setting up project..."

# Check OS type
OS="$(uname -s)"
if [[ "$OS" != "Linux" && "$OS" != "Darwin" ]]; then
  echo "Unsupported OS: $OS"
  echo "Use WSL or Git Bash on Windows"
  exit 1
fi

# Checking uv installation
if ! command -v uv &> /dev/null; then
  echo "uv is not installed."
  echo "Install it from: https://docs.astral.sh/uv/"
  exit 1
fi

# Create venv
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  uv venv .env
else
  echo "Virtual environment already exists"
fi

# Activateing virtual environment
source .env/bin/activate

# Install dependencies
echo "Installing dependencies..."
uv pip install -e .

# Doing sanity checks
python --version
uv --version

echo ""
echo "Setup complete!"
echo "To activate later: source .venv/bin/activate"