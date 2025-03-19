FROM harbor1.fisgeo.unipg.it/uninuvola/unihubsingle:latest

USER root

RUN apt update && \
    apt install -y zip unzip unrar-free openssh-client htop procps nano less tmux screen vim curl git flatpak

RUN echo "exec /bin/bash" >> /etc/profile

USER jovyan

RUN flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo && \
    flatpak install flathub org.mozilla.firefox && flatpak install flathub org.chromium.Chromium
