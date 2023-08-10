FROM ubuntu:focal

# Use noninteractive to suppress prompt to configure keyboard layout
ENV DEBIAN_FRONTEND=noninteractive

# Install prerequisites
RUN apt-get update && apt-get install --assume-yes curl gnupg

# Add microsoft public key and repository
RUN curl https://packages.microsoft.com/keys/microsoft.asc \
    | gpg --dearmor | tee /usr/share/keyrings/microsoft.gpg \
    && echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main' \
    > /etc/apt/sources.list.d/microsoft.list

# Install package
RUN apt-get update && apt-get install --assume-yes code

# Make docker container image more compact
RUN rm -rf /var/lib/apt/lists/*
