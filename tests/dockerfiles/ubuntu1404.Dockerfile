FROM ubuntu:14.04

RUN apt-get update && \
    apt-get install -y python

ENTRYPOINT ["tail", "-f", "/dev/null"]
