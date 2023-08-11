FROM ubuntu:focal

# Use noninteractive to suppress prompt to configure keyboard layout
ENV DEBIAN_FRONTEND=noninteractive

# Install prerequisites
RUN apt-get update && apt-get install --assume-yes curl gpg

# Add google public key and repository
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg \
    | gpg --dearmor | tee /usr/share/keyrings/google.gpg \
    && echo 'deb [signed-by=/usr/share/keyrings/google.gpg] http://packages.cloud.google.com/apt google-compute-engine-focal-stable main' \
    > /etc/apt/sources.list.d/google.list

# Install agent
RUN apt-get update && apt-get install --assume-yes google-osconfig-agent

# Make docker container image more compact
RUN rm -rf /var/lib/apt/lists/*
