FROM harbor1.fisgeo.unipg.it/uninuvola/conda:latest

USER root 

RUN apt update && \
    apt install -y gnupg software-properties-common && \
    mkdir -m755 -p /etc/apt/keyrings && \
    wget -O /etc/apt/keyrings/qgis-archive-keyring.gpg https://download.qgis.org/downloads/qgis-archive-keyring.gpg && \
    echo "deb [signed-by=/etc/apt/keyrings/qgis-archive-keyring.gpg] https://qgis.org/debian bullseye main" > /etc/apt/sources.list.d/qgis.list && \
    apt update && \
    apt install -y qgis qgis-plugin-grass

#RUN apt update && \
#    apt install -y  gnupg software-properties-common && \
#    mkdir -m755 -p /etc/apt/keyrings && \
#    wget -O /etc/apt/keyrings/qgis-archive-keyring.gpg https://download.qgis.org/downloads/qgis-archive-keyring.gpg && \
#    touch  /etc/apt/sources.list.d/qgis.sources && \
#    echo "Types: deb deb-src \
#          URIs: https://qgis.org/debian \
#          Suites: bullseye \
#          Architectures: amd64 \
#          Components: main \
#          Signed-By: /etc/apt/keyrings/qgis-archive-keyring.gpg"  >  /etc/apt/sources.list.d/qgis.sources && \
#    apt update && \
#    apt install -y  qgis qgis-plugin-grass

RUN apt-get install -y grass grass-doc

RUN apt update && \
    apt install -y gnupg software-properties-common && \
    add-apt-repository ppa:flatpak/stable && \
    apt update && \
    apt install -y flatpak && \
    apt install -y gnome-software-plugin-flatpak && \
    flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo  && \
    flatpak install -y flathub org.cloudcompare.CloudCompare

RUN apt-get install -y openmpi-bin && \
    wget https://plus.swat.tamu.edu/downloads/2.3/2.3.1/swatplus-linux-installer-2.3.1.tgz && \
    mkdir swatplus && \ 
    cd swatplus && \
    tar -zxvf swatplus-linux-installer-2.3.1.tgz && \
    /bin/bash -c installforall.sh && \
    rm swatplus-linux-installer-2.3.1.tgz

RUN echo "exec /bin/bash" >> /etc/profile
USER jovyan

