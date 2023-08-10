FROM ubuntu:focal

# Use noninteractive to suppress prompt to configure keyboard layout
ENV DEBIAN_FRONTEND=noninteractive

# Install prerequisites
RUN apt-get update && apt-get install --assume-yes software-properties-common

# Add r repository and public key
RUN apt-key adv --keyserver keyserver.ubuntu.com \
    --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 && \
    add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'

# Install package
RUN apt-get update && \
    apt-get install --assume-yes r-base

# Make docker container image more compact
RUN rm -rf /var/lib/apt/lists/*
