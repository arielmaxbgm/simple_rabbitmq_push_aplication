#!/bin/bash
# script that fetch de rabbit container's IP and replace the config file

# Inspect docker containers to find the rabbitmq's IP
docker_id=$(sudo docker ps | grep rabbit | awk '{print $1}')
rabbit_ip=$(sudo docker inspect -f '{{ .NetworkSettings.IPAddress }}' $docker_id)

# Update the ini file to put the correct value
sed -i -r -s "s/msg_bus_host=.*/msg_bus_host=$rabbit_ip/" config.ini
