ARG GIT_BRANCH

FROM harbor1.fisgeo.unipg.it/uninuvola/base:${GIT_BRANCH}

USER root

RUN apt update && \
    apt install -y zip unzip unrar-free openssh-client htop procps nano less tmux screen vim curl git gfortran cmake build-essential pkg-config

# Golang
RUN wget -O go.tar.gz https://dl.google.com/go/go1.24.2.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go.tar.gz && \
    rm go.tar.gz

RUN echo "export PATH=\$PATH:/usr/local/go/bin" > /etc/profile.d/go.sh

USER jovyan
