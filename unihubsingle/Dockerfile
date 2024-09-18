FROM quay.io/jupyterhub/k8s-singleuser-sample:3.3.8
MAINTAINER Mirko Mariotti <mirko.mariotti@unipg.it>

USER root

RUN apt update

RUN apt install -y --no-install-recommends build-essential ca-certificates wget curl

RUN wget -O "/usr/share/keyrings/xpra.asc" https://xpra.org/xpra.asc

RUN cd /etc/apt/sources.list.d && wget https://raw.githubusercontent.com/Xpra-org/xpra/master/packaging/repos/bullseye/xpra.sources

RUN apt update

RUN apt install -y --no-install-recommends iproute2 xpra-x11 xpra xpra-html5 git curl xterm xauth

RUN apt install -y --no-install-recommends rclone fuse3

RUN apt install -y --no-install-recommends chromium

RUN apt install -y --no-install-recommends sudo psmisc coreutils

RUN rm -f /etc/mtab && ln -s /proc/mounts /etc/mtab

RUN apt install -y --no-install-recommends python3-paramiko python3-pil python3-dbus python3-uinput python3-xdg python3-pyinotify

#RUN adduser jovyan sudo
#RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

#RUN chown -R jovyan:jovyan /usr/local/share/jupyter

#USER root
#USER jovyan

ENV NODE_VERSION=20.10.0
#ENV NODE_VERSION=22.2.0
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
ENV NVM_DIR=/home/jovyan/.nvm
RUN . "$NVM_DIR/nvm.sh" && nvm install ${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm use v${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm alias default v${NODE_VERSION}
ENV PATH="/root/.nvm/versions/node/v${NODE_VERSION}/bin/:${PATH}"

RUN . "$NVM_DIR/nvm.sh" && pip install git+https://github.com/FZJ-JSC/jupyter-xprahtml5-proxy.git
#RUN . "$NVM_DIR/nvm.sh" && pip install paramiko python-uinput pyinotify xdg ldmud-dbus jupyter-server-proxy 

#RUN . "$NVM_DIR/nvm.sh" && jupyter labextension enable @jupyterlab/server-proxy
#RUN . "$NVM_DIR/nvm.sh" && jupyter labextension enable @jupyterhub/jupyter-server-proxy
RUN . "$NVM_DIR/nvm.sh" && jupyter labextension list
RUN . "$NVM_DIR/nvm.sh" && jupyter lab build

USER jovyan
