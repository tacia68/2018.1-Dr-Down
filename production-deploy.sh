#!/bin/bash
#
# Purpose: Continuous deploy on production environment
#
# Author: João Pedro Sconetto <sconetto.joao@gmail.com>

docker tag 20181-dr-down_django:latest $DOCKER_ID_USER/20181-dr-down_django
docker push $DOCKER_ID_USER/20181-dr-down_django

sudo apt-get install sshpass -y
sshpass -p $SSH_PASSWORD ssh drdown@159.203.182.32 '/bin/bash /home/drdown/deploy.sh'
