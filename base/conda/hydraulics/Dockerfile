FROM harbor1.fisgeo.unipg.it/uninuvola/conda:latest

USER root 

RUN apt update && \
    apt install gnupg software-properties-common && \
    mkdir -m755 -p /etc/apt/keyringsi && \
    wget -O /etc/apt/keyrings/qgis-archive-keyring.gpg https://download.qgis.org/downloads/qgis-archive-keyring.gpg && \
    echo "Types: deb deb-src \
          URIs: https://qgis.org/debian\
          Suites: your-distributions-codename\
          Architectures: amd64 \
          Components: main \
          Signed-By: /etc/apt/keyrings/qgis-archive-keyring.gpg"  >>  /etc/apt/sources.list.d/qgis.sources && \
          apt update && apt install qgis qgis-plugin-grass

RUN apt-get install grass grass-doc

RUN apt install flatpak && \
    add-apt-repository ppa:flatpak/stable && \
    apt update && \  
    apt install flatpak && \ 
    apt install gnome-software-plugin-flatpak && \
    flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo && \ 
    flatpak install -y flathub org.cloudcompare.CloudCompare

RUN apt-get install openmpi-bin && \
    wget https://plus.swat.tamu.edu/downloads/2.3/2.3.1/swatplus-linux-installer-2.3.1.tgz && \
    mkdir swatplus && \ 
    cd swatplus && \
    tar -zxvf swatplus-linux-installer-2.3.1.tgz
    bash installforall.sh
    rm swatplus-linux-installer-2.3.1.tgz

RUN echo "exec /bin/bash" >> /etc/profile
USER jovyan

