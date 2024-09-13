FROM quay.io/jupyterhub/k8s-singleuser-sample:3.3.8
MAINTAINER Mirko Mariotti <mirko.mariotti@unipg.it>

USER root

RUN apt update

RUN apt install -y --no-install-recommends iproute2 xpra git curl xterm 

RUN apt install -y --no-install-recommends build-essential

#RUN apt-get install -y --no-install-recommends python3-cryptography python3-pil

RUN apt install -y --no-install-recommends rclone fuse3

RUN apt install -y --no-install-recommends chromium

RUN apt install -y --no-install-recommends sudo psmisc coreutils

RUN rm -f /etc/mtab && ln -s /proc/mounts /etc/mtab

USER jovyan

#ENV NODE_VERSION=20.10.0
#RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
#ENV NVM_DIR=/home/jovyan/.nvm
#RUN . "$NVM_DIR/nvm.sh" && nvm install ${NODE_VERSION}
#RUN . "$NVM_DIR/nvm.sh" && nvm use v${NODE_VERSION}
#RUN . "$NVM_DIR/nvm.sh" && nvm alias default v${NODE_VERSION}
#ENV PATH="/root/.nvm/versions/node/v${NODE_VERSION}/bin/:${PATH}"
#
#RUN . "$NVM_DIR/nvm.sh" && pip install git+https://github.com/FZJ-JSC/jupyter-xprahtml5-proxy.git
#RUN . "$NVM_DIR/nvm.sh" && pip install paramiko python-uinput pyinotify xdg ldmud-dbus 
#
#USER root
#
#RUN . "$NVM_DIR/nvm.sh" && jupyter labextension install @jupyterlab/server-proxy
#RUN . "$NVM_DIR/nvm.sh" && jupyter lab build
#
#USER jovyan
