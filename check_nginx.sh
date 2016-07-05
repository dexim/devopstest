#!/bin/bash

port=$(sudo netstat -taupen | grep nginx | grep -v tcp6| awk '{print $4}' | awk -F ":" '{print $2}')
hname=$(exec hostname)
if [ "$port"=="80" ]; then
    echo "Nginx on $hname is listening on port 80"
    ip=$(curl http://$hname 2> /dev/null | grep 'Server' | grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}")
    echo "Check serving the content correctly. Server IP: $ip"; 
else 
    echo "Nginx on $hname fails to listen on port 80"
fi
