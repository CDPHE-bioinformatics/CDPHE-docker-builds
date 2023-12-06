FROM ubuntu:focal

# Use noninteractive to suppress prompt to configure keyboard layout
ENV DEBIAN_FRONTEND=noninteractive

# Install prerequisites
RUN apt-get update && apt-get upgrade -y && apt-get install -y curl

# Download binary and install
RUN curl -o /usr/local/bin/bs \
    "https://launch.basespace.illumina.com/CLI/latest/amd64-linux/bs" \
    && chmod u+x /usr/local/bin/bs

# Make docker container image more compact
RUN rm -rf /var/lib/apt/lists/*
