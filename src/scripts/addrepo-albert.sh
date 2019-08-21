#!/bin/bash

# Installing the GPG key
curl https://build.opensuse.org/projects/home:manuelschneid3r/public_key | sudo apt-key add -

# Based 18.04
#sudo sh -c "echo 'deb http://download.opensuse.org/repositories/home:/manuelschneid3r/xUbuntu_18.04/ /' > /etc/apt/sources.list.d/home:manuelschneid3r.list"
# Based 19.04
sudo sh -c "echo 'deb http://download.opensuse.org/repositories/home:/manuelschneid3r/xUbuntu_19.04/ /' > /etc/apt/sources.list.d/home:manuelschneid3r.list"

