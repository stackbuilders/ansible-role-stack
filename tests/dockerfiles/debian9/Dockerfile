FROM debian:9

RUN apt-get update && \
    apt-get install -y \
    python \
    openssh-server \
    dbus \
    && rm -rf /var/lib/apt/lists/*

RUN touch /var/log/auth.log

CMD ["/lib/systemd/systemd"]
