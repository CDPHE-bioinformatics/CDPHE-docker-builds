# CDPHE Analysis Virtual Machine

The code here is from the Colorado Deparment of Public Health and Environment's
(CDPHE) bioinformatic genomic surveillance group. This directory contains the
Dockerfile that has an installation setup that matches the base Google Cloud
Platform (GCP) virtual machine that we use for analysis.

## Requirements

- Docker
- Google Cloud Platform

## Software Installed

We use many software packages for analysis. The software listed here is what is
installed as a base image for our bioinformaticians to use. It is the common or
shared list that we all use and isn't therefore inclusive of what we install
individually. Note also includes Google Cloud agents.

1. Google Chrome Remote Desktop
2. Google Config and Ops Agents
3. Google Cloud Tools
4. Jupyter Core and Client
5. Docker
6. Java

### Optimized Dockerfile

To reduce the size and improve building a container from our prerequisites, we
list the full installation below but remove duplicate software/packages from
the Dockerfile.

### Google Chrome Remote Desktop

Directions are taken from Google's [documentation](https://cloud.google.com/architecture/chrome-desktop-remote-on-compute-engine).

```docker
FROM ubuntu:focal

ENV DEBIAN_FRONTEND=noninteractive

RUN curl -L -o chrome-remote-desktop_current_amd64.deb \
    https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb

RUN apt update && \
    apt install --assume-yes ./chrome-remote-desktop_current_amd64.deb && \
    apt install --assume-yes xfce4 desktop-base dbus-x11 xscreensaver && \
    apt install --assume-yes task-xfce-desktop

RUN echo "exec /etc/X11/Xsession /usr/bin/xfce4-session" > /etc/chrome-remote-desktop-session

RUN systemctl disable lightdm.service
```
