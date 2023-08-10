FROM ubuntu:focal

# Use noninteractive to suppress prompt to configure keyboard layout
ENV DEBIAN_FRONTEND=noninteractive

# Install package
FROM docker as java

RUN apt-get update && apt-get install --assume-yes openjdk-8-jre
