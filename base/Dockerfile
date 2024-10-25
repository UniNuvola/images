FROM harbor1.fisgeo.unipg.it/uninuvola/unihubsingle:latest

USER root

RUN apt-get update && \
    apt-get install -y unzip openssh-client htop

RUN echo "exec /bin/bash" >> /etc/profile

USER jovyan
