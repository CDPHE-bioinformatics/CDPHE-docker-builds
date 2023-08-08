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

1. Chrome Remote Desktop
2. Google Config and Ops Agents
3. Google Cloud CLI
4. Docker
5. Java
6. Jupyter Core and Client

## Container Design

To ease testing and therefore deployment, each of the listed software have there
own Dockerfile in their respective folders.

### Optimized Dockerfile

To reduce the size and improve building a container from our prerequisites, we
list the full installation below but remove duplicate software/packages from
the Dockerfile.
