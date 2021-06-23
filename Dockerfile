# Container image that runs your code
FROM ubuntu:20.04

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh


RUN apt update -y

RUN apt install python3-pip -y

RUN pip install flawfinder

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
