FROM harbor1.fisgeo.unipg.it/uninuvola/unihubsingle:latest

USER root

RUN apt update && \
    apt install -y zip unzip unrar-free openssh-client htop procps nano less tmux screen vim curl git && \
    snap install firefox chromium

RUN echo "exec /bin/bash" >> /etc/profile

USER jovyan
