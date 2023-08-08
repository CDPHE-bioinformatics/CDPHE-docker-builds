FROM ubuntu:focal

# Use noninteractive to suppress prompt to configure keyboard layout
ENV DEBIAN_FRONTEND=noninteractive

# Install prerequisites
RUN apt-get update && apt-get install --assume-yes curl gnupg

# Add google repository and public key
RUN echo "deb https://packages.cloud.google.com/apt cloud-sdk main" > \
    /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | \
    apt-key add -

# Install agent
RUN apt-get update && \
    apt-get install --assume-yes google-cloud-cli

# Make docker container image more compact
RUN rm -rf /var/lib/apt/lists/*
