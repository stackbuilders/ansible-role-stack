FROM base/archlinux

RUN pacman -Sy --noconfirm python

ENTRYPOINT ["tail", "-f", "/dev/null"]
