FROM harbor1.fisgeo.unipg.it/uninuvola/unihubsingle:latest

USER root

RUN apt update && \
    apt install -y zip unzip unrar openssh-client htop procps nano less tmux screen vim 

RUN echo "exec /bin/bash" >> /etc/profile

USER jovyan
