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
    apt-get install -y curl gnupg ca-certificates && \
    curl -sSO https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.sh && \
    bash add-google-cloud-ops-agent-repo.sh --also-install && \
    rm -rf /var/lib/apt/lists/*

COPY ops-agent-config.yaml /etc/google-cloud-ops-agent/config.yaml

CMD ["/usr/sbin/google_cloud_ops_agent"]

# GCP Monitoring agent addin
FROM ops-agent AS monitoring-agent

RUN apt-get update && \
    apt-get install -y curl gnupg2

RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -

RUN echo "deb http://packages.cloud.google.com/apt google-cloud-monitoring-bionic main" > /etc/apt/sources.list.d/google-cloud-monitoring.list

RUN apt-get update && \
    apt-get install -y stackdriver-agent && \
    rm -rf /var/lib/apt/lists/*

CMD ["/usr/sbin/stackdriver-agent", "--no-start"]

# Google Cloud
FROM monitoring-agent AS gcloud
RUN apt-get update && \
    apt-get install apt-transport-https ca-certificates gnupg

RUN echo "deb https://packages.cloud.google.com/apt cloud-sdk main" > /etc/apt/sources.list.d/google-cloud-sdk.list

RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -

RUN apt-get update && \
    apt-get install -y google-cloud-cli && \
    rm -rf /var/lib/apt/lists/*

# Dockerfile meta
LABEL description="This image contains all tools base/prior to analysis or development."
LABEL website="https://github.com/CDPHE/docker-builds"
LABEL license="https://github.com/CDPHE/docker-builds/blob/master/LICENSE"
LABEL maintainer="Daniel Polanco"
LABEL maintainer.email="daniel.polanco@state.co.us"

# Set workdir for analysis
WORKDIR /data