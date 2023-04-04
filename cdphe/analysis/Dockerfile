ARG DEBIAN_FRONTEND=noninteractive

FROM ubuntu:focal AS stock

ENV DEBIAN_FRONTEND=${DEBIAN_FRONTEND}

RUN apt-get update && \
    apt-get install -y \
        desktop-base \
        git-all \
        jupyter-client \
        jupyter-core \
        libzmq3-dev \
        libcurl4-openssl-dev \
        libssl-dev \
        openjdk-8-jre \
        tasksel \
        wget \
        xfce4 \
        xscreensaver && \
    rm -rf /var/lib/apt/lists/*

FROM stock AS monitor

RUN apt-get update && \
    apt-get install -y curl gnupg ca-certificates && \
    curl -sSO https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.sh && \
    bash add-google-cloud-ops-agent-repo.sh --also-install && \
    rm -rf /var/lib/apt/lists/*

LABEL description="This image contains all tools base/prior to analysis or development."
LABEL website="https://github.com/CDPHE/docker-builds"
LABEL license="https://github.com/CDPHE/docker-builds/blob/master/LICENSE"
LABEL maintainer="Daniel Polanco"
LABEL maintainer.email="daniel.polanco@state.co.us"

WORKDIR /data