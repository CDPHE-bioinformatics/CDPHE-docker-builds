FROM ubuntu:focal

# Use noninteractive to suppress prompt to configure keyboard layout
ENV DEBIAN_FRONTEND=noninteractive

# Install prerequisites
RUN apt-get update && apt-get install --assume-yes curl gnupg

# Add VS Code repository and public key
RUN curl https://packages.microsoft.com/keys/microsoft.asc \
    | gpg --dearmor > /etc/apt/trusted.gpg.d/microsoft.gpg \
    && echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" \
    > /etc/apt/sources.list.d/vscode.list

# Install package
RUN apt-get update && apt-get install --assume-yes code
