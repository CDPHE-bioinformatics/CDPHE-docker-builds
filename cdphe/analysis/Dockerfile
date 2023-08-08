ARG DEBIAN_FRONTEND=noninteractive

# Stock setup
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

# GCP Ops agent addin
FROM stock AS ops-agent

RUN apt-get update && \
    apt-get install -y curl gnupg && \
    curl -sSO https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.sh && \
    bash add-google-cloud-ops-agent-repo.sh --also-install && \
    rm -rf /var/lib/apt/lists/*

COPY ./google_ops_agent/ops-agent-config.yaml /etc/google-cloud-ops-agent/config.yaml

# Google OS Config Agent
FROM ops-agent AS os-config-agent

RUN echo 'deb http://packages.cloud.google.com/apt google-compute-engine-focal-stable main' > \
    /etc/apt/sources.list.d/google-compute-engine.list

RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | \
    apt-key add -

RUN apt-get update && \
    apt-get install -y google-osconfig-agent

# Google Cloud
FROM os-config-agent AS gcloud

RUN apt-get update && \
    apt-get install -y curl gnupg

RUN echo "deb https://packages.cloud.google.com/apt cloud-sdk main" > /etc/apt/sources.list.d/google-cloud-sdk.list

RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -

RUN apt-get update && \
    apt-get install -y google-cloud-cli && \
    rm -rf /var/lib/apt/lists/*

# Chrome remote desktop
FROM gcloud AS chrome-remote-desktop

RUN curl -L -o chrome-remote-desktop_current_amd64.deb \
    https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb

RUN apt-get update && \
    apt-get install --assume-yes ./chrome-remote-desktop_current_amd64.deb && \
    apt-get install --assume-yes xfce4 desktop-base dbus-x11 xscreensaver && \
    rm -rf /var/lib/apt/lists/*

RUN echo "exec /etc/X11/Xsession /usr/bin/xfce4-session" > /etc/chrome-remote-desktop-session

RUN systemctl disable lightdm.service

FROM chrome-remote-desktop AS docker

RUN apt-get update && apt-get install --assume-yes curl gnupg

RUN echo "deb https://download.docker.com/linux/ubuntu focal stable" > \
    /etc/apt/sources.list.d/docker.list && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
    apt-key add -

RUN apt-get update && \
    apt-get install --assume-yes docker-ce

RUN rm -rf /var/lib/apt/lists/*

FROM docker as java

RUN apt-get update && apt-get install --assume-yes openjdk-8-jre

FROM java as r

RUN apt-get update && apt-get install --assume-yes software-properties-common

RUN apt-key adv --keyserver keyserver.ubuntu.com \
    --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 && \
    add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'

RUN apt-get update && \
    apt-get install --assume-yes r-base

RUN rm -rf /var/lib/apt/lists/*

# Dockerfile meta
LABEL description="This image contains all tools base/prior to analysis or development."
LABEL website="https://github.com/CDPHE/docker-builds"
LABEL license="https://github.com/CDPHE/docker-builds/blob/master/LICENSE"
LABEL maintainer="Daniel Polanco"
LABEL maintainer.email="daniel.polanco@state.co.us"

# Set workdir for analysis
WORKDIR /data
