FROM ubuntu:focal

# Use noninteractive to suppress prompt to configure keyboard layout
ENV DEBIAN_FRONTEND=noninteractive

# Install prerequisites
RUN apt-get update && apt-get install --assume-yes curl gnupg

# Add google repository for Ubuntu and public key
RUN echo 'deb http://packages.cloud.google.com/apt google-compute-engine-focal-stable main' > \
    /etc/apt/sources.list.d/google-compute-engine.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | \
    apt-key add -

# Install agent
RUN apt-get update && \
    apt-get install --assume-yes google-osconfig-agent

# Make docker container image more compact
RUN rm -rf /var/lib/apt/lists/*
