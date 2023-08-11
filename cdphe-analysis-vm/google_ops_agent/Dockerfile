FROM ubuntu:focal

# Use noninteractive to suppress prompt to configure keyboard layout
ENV DEBIAN_FRONTEND=noninteractive

# Install prerequisites
RUN apt-get update && apt-get install --assume-yes curl gpg

# Download script, install and agent is started automaticaly
RUN curl -sSO https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.sh \
    && bash add-google-cloud-ops-agent-repo.sh --also-install

# Copy generic configuration file
COPY ops-agent-config.yaml /etc/google-cloud-ops-agent/config.yaml

# Make docker container image more compact
RUN rm -rf /var/lib/apt/lists/*
