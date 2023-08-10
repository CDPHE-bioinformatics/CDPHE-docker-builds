FROM ubuntu:focal

# Use noninteractive to suppress prompt to configure keyboard layout
ENV DEBIAN_FRONTEND=noninteractive

# Install package
RUN apt-get update && apt-get install --assume-yes openjdk-8-jre

# Make docker container image more compact
RUN rm -rf /var/lib/apt/lists/*
