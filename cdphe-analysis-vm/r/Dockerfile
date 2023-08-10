FROM ubuntu:focal

# Use noninteractive to suppress prompt to configure keyboard layout
ENV DEBIAN_FRONTEND=noninteractive

# Install prerequisites
RUN apt-get update && apt-get install --assume-yes software-properties-common

# Add r repository and public key
RUN gpg --recv-keys --keyserver keyserver.ubuntu.com E298A3A825C0D65DFD57CBB651716619E084DAB9 \
    && gpg --export E298A3A825C0D65DFD57CBB651716619E084DAB9 \
    > /usr/share/keyrings/r-base.gpg \
    && gpg --batch --yes --delete-key E298A3A825C0D65DFD57CBB651716619E084DAB9 \
    && echo 'deb [signed-by=/usr/share/keyrings/r-base.gpg] https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/' \
    > /etc/apt/sources.list.d/r-base.list

# Install package
RUN apt-get update && apt-get install --assume-yes r-base

# Make docker container image more compact
RUN rm -rf /var/lib/apt/lists/*
