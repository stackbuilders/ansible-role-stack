FROM debian:8

RUN apt-get update && \
    apt-get install -y python

ENTRYPOINT ["tail", "-f", "/dev/null"]
