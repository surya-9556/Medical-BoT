# Medical-BoT

Medical-BoT is an end-to-end medical question-answering chatbot that uses Retrieval-Augmented Generation (RAG) over a curated medical knowledge base to provide accurate and explainable responses to user queries.

## Features

* Retrieval-Augmented Generation using a FAISS vector store built from structured medical documents.
* Modular application layout with clear separation of components, configuration, and shared utilities.
* Web application interface powered by an `application.py` entrypoint under the `app` package.
* Containerized deployment using a production-ready Dockerfile.
* CI/CD-ready with a Jenkinsfile for automated builds, tests, and deployment pipelines.
* Python project metadata and dependency management via `pyproject.toml`, `setup.py`, and `uv.lock`.

## Project Structure

```text
Medical-BoT/
├── Vectorstore/
│   └── df_faiss/           # Persisted FAISS index and related vector store artifacts
├── app/
│   ├── common/             # Shared utilities and helper functions
│   ├── components/         # Core application components (routes, services, etc.)
│   ├── config/             # Configuration files and settings
│   ├── templates/          # Frontend templates for the web UI
│   ├── __init__.py         # App package initialization
│   └── application.py      # Main application entrypoint
├── custom_jenkins/         # Custom Jenkins-related scripts/configurations
├── data/                   # Source medical data and processed artifacts
├── .gitignore
├── .python-version
├── Dockerfile
├── Jenkinsfile
├── main.py                 # Top-level runner or bootstrap script
├── pyproject.toml
├── setup.py
└── uv.lock
```

## Getting Started

### Prerequisites

* Python (version specified in `.python-version`)
* Docker (optional, for containerized runs)
* Jenkins (optional, if you plan to use the provided CI/CD pipeline)

### Clone the Repository

```bash
git clone https://github.com/surya-9556/Medical-BoT.git
cd Medical-BoT
```

### Create and Activate a Virtual Environment

Use your preferred virtual environment tool (e.g., `venv`, `conda`, or `uv`):

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### Install Dependencies

If you are using **uv**:

```bash
uv sync
```

Or with standard tools (depending on how `pyproject.toml` / `setup.py` is configured):

```bash
pip install -e .
```

## Running the Application

### Local Run via Python

The repository includes `main.py` and an application module under `app/application.py`. Typical ways to run the service are:

```bash
python main.py
```

or:

```bash
python -m app.application
```

Once started, the web interface should be available at a local URL such as:

* `http://127.0.0.1:8000`, or
* `http://127.0.0.1:5000`

(depending on the framework and configuration—see `application.py` for the exact host and port).

### Run with Docker

Build the image:

```bash
docker build -t medical-bot .
```

Run the container:

```bash
docker run -p 8000:8000 medical-bot
```

Adjust the exposed port if the application uses a different internal port.

## Data and Vector Store

* The `data/` directory is intended for raw and processed medical documents used to power the chatbot.
* The `Vectorstore/df_faiss/` directory holds the FAISS index and associated files for efficient similarity search.

If you modify or add new medical data, you will typically need to:

1. Preprocess the data into chunks or documents.
2. Rebuild the FAISS index and save it under `Vectorstore/df_faiss/`.

(Refer to your internal data-preparation scripts or notebooks for the exact pipeline.)

## CI/CD with Jenkins

This repository is prepared for automated pipelines:

* `Jenkinsfile` defines the main Jenkins pipeline stages (build, test, deploy, etc.).
* `custom_jenkins/` can hold custom scripts, shared libraries, or configuration for Jenkins agents.

To use it:

1. Configure a Jenkins job pointing to this repository.
2. Ensure required environment variables and credentials are set in Jenkins.
3. Trigger the pipeline; Jenkins will follow the stages defined in the `Jenkinsfile`.

## Configuration

The `app/config/` directory contains configuration modules or files for environment variables, model paths, and vector store locations.

Update configuration there to point to your own data, vector store, or external services as needed.