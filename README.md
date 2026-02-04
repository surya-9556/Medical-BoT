# Medical-BoT: My Enterprise-Grade Medical RAG Chatbot

## Overview
I built **Medical-BoT**, an **end-to-end, production-ready medical question-answering chatbot** that uses **Retrieval-Augmented Generation (RAG)** to provide accurate, context-aware, and explainable responses to user queries. My focus was on creating a **modular architecture** with integrated **CI/CD pipelines, containerization, and cloud deployment**, reflecting **real-world enterprise AI engineering practices**.

This project showcases my skills in **AI development, cloud deployment, and MLOps**, making it ideal for senior recruiters and technical leadership to evaluate my hands-on expertise.

---

## Key Features
- I implemented **RAG** using a FAISS vector store built from structured medical documents.
- Designed a **modular architecture** with clear separation of components, configuration, and utilities.
- Enabled **fast setup** using `./setup.sh` and **UV** for deterministic dependency management.
- Developed a **web interface** via `app/application.py`.
- Exposed a **REST API** using **FastAPI** for scalable, low-latency requests.
- Orchestrated **LangChain + Groq + FAISS + HuggingFace embeddings** for semantic search and context-aware responses.
- Performed NLP preprocessing using **spaCy** and **NLTK**.
- Containerized the application with **Docker** for reproducibility.
- Set up **CI/CD pipelines with Jenkins** for automated build, test, and deployment.
- Integrated **SonarQube** for code quality and security checks.
- Deployed to the cloud using **AWS ECR + AWS App Runner / EKS Free Tier**.

---

## Tech Stack
| Layer | Tools / Libraries |
|-------|-----------------|
| Version Control & CI/CD | GitHub + **Jenkins** |
| Containerization | Docker (UV inside image for fast setup) |
| Cloud Deployment | AWS ECR + AWS App Runner / EKS (Free Tier) |
| Retrieval & NLP | LangChain, FAISS, HuggingFace, Sentence-Transformers, spaCy, NLTK |
| API / Web Interface | FastAPI + Streamlit |
| OS / Setup | `./setup.sh` for one-command setup, managed by **UV** |

---

## Why I Used UV
I chose **UV** over pip for dependency management and running the application because it offers several advantages:

- **Faster dependency installation** – significantly reduces setup time.
- **Deterministic environments** – lockfile-based installs ensure reproducibility.
- **Cleaner CI/CD pipelines** – simplifies automated builds and deployments.
- **Optimized container performance** – lightweight and consistent installations in Docker.
- **Enterprise-ready tooling** – increasingly adopted in production-grade Python systems.

Example commands I use:
```bash
uv sync          # Install dependencies
uv run app.main  # Run the application
```
This ensures **consistency across local, CI/CD, and cloud deployments**.

---

## Quick Start

### 1. Clone the Project
```bash
git clone https://github.com/<your-username>/Medical-BoT.git
cd Medical-BoT
```

### 2. Run Setup
```bash
chmod +x setup.sh
./setup.sh
```
> This installs all dependencies with **UV**, prepares Docker containers, and sets up the environment.

### 3. Start the Application
```bash
docker compose up
```
- The API is accessible at: `http://localhost:8000`  
- You can ask medical queries and receive **context-aware responses** from the knowledge base.

Or locally via Python:
```bash
python main.py
# or
python -m app.application
```

---

## Data and Vector Store
- `data/`: Contains raw and processed medical documents used by the chatbot.
- `Vectorstore/df_faiss/`: Contains the persisted FAISS index for fast semantic search.

**To update the vector store:**
1. Preprocess new medical documents into chunks.
2. Rebuild the FAISS index in `Vectorstore/df_faiss/`.

---

## CI/CD & Code Quality
I set up automated CI/CD using Jenkins and ensured code quality with SonarQube:
- **Jenkinsfile** defines the build, test, and deployment stages.
- **custom_jenkins/** contains scripts and configurations for Jenkins agents.
- **SonarQube** performs static analysis, maintainability checks, and security scans.

Steps I follow:
1. Configure a Jenkins job pointing to this repository.
2. Set required environment variables and credentials.
3. Trigger the pipeline to build, test, scan, and deploy Docker images to AWS ECR / EKS.

---

## Cloud Deployment
- I push Docker images to **AWS ECR**.
- Deploy the application via **AWS App Runner** or **AWS EKS Free Tier**.
- Designed for horizontal scaling, rolling updates, and enterprise-ready cloud orchestration.

---

## Configuration
- `app/config/`: Contains environment variables, model paths, and vector store locations.
- I update configurations to point to my own data, vector store, or external services as needed.

---

## Future Enhancements
- Implement multi-document ingestion pipeline and dynamic updates.
- Improve **query ranking and relevance scoring**.
- Add user authentication, logging, and monitoring.
- Expand knowledge base beyond PDFs.
- Introduce agent memory and advanced task coordination.