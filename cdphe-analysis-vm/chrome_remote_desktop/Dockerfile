FROM ubuntu:focal

# Use noninteractive to suppress prompt to configure keyboard layout
ENV DEBIAN_FRONTEND=noninteractive

# Install prerequisites
RUN apt-get update && apt-get install --assume-yes curl

# Download deb package and install Chrome Remote Desktop
RUN curl -L -o chrome-remote-desktop_current_amd64.deb \
    https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb \
    && apt-get install --assume-yes ./chrome-remote-desktop_current_amd64.deb

# Install Xfce and basic desktop components plus xscreensaver for compatibility
RUN apt-get install --assume-yes xfce4 desktop-base dbus-x11 xscreensaver

# Use Xfce by default for Chrome Remote Desktop
RUN echo "exec /etc/X11/Xsession /usr/bin/xfce4-session" \
    > /etc/chrome-remote-desktop-session

# Disable lightdm since there isn't a display connected to the instance
RUN systemctl disable lightdm.service

# Make docker container image more compact
RUN rm -rf /var/lib/apt/lists/*
