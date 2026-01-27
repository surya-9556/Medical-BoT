# Jenkins LTS base image
FROM jenkins/jenkins:lts

# Switch to root to install system packages
USER root

# Install Docker from Debian repositories (Trixie-safe)
RUN apt-get update && apt-get install -y \
    docker.io \
    docker-cli \
    containerd \
    ca-certificates \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Ensure docker group exists and add jenkins user
RUN groupadd -f docker && usermod -aG docker jenkins

# Optional: Docker data directory (useful for DinD-style usage)
VOLUME /var/lib/docker

# Switch back to Jenkins user
USER jenkins
