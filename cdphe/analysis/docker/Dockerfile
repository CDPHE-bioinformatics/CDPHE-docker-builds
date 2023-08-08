FROM ubuntu:focal

# Use noninteractive to suppress prompt to configure keyboard layout
ENV DEBIAN_FRONTEND=noninteractive

# Install prerequisites
RUN apt-get update && apt-get install --assume-yes curl gnupg

# Add docker repository and public key
RUN echo "deb https://download.docker.com/linux/ubuntu focal stable" > \
    /etc/apt/sources.list.d/docker.list && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
    apt-key add -

# Install package
RUN apt-get update && \
    apt-get install --assume-yes docker-ce

# Make docker container image more compact
RUN rm -rf /var/lib/apt/lists/*
