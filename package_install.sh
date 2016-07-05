#!/bin/bash

#Check if package installed
if [ $(dpkg-query -W -f='${Status}' $1 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  echo "Package $1 is not installed."
  sudo apt-get update
  sudo apt-get --force-yes --yes install $1
else
  echo "Package $1 already installed."
fi
