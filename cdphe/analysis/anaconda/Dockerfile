FROM ubuntu:focal

# Use noninteractive to suppress prompt to configure keyboard layout
ENV DEBIAN_FRONTEND=noninteractive

# Install prerequisites
COPY --from=continuumio/anaconda:latest /opt/conda /opt/conda

# Add conda to path
ENV PATH "$PATH:/opt/conda/bin"

# Make docker container image more compact
RUN rm -rf /var/lib/apt/lists/*

# Recommended: to run anaconda without root privileges (i.e. sudo)
# https://docs.anaconda.com/free/anaconda/install/multi-user/
