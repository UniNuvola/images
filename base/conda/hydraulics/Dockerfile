FROM harbor1.fisgeo.unipg.it/uninuvola/conda:latest

USER root 

RUN apt update && \
    apt install -y gnupg software-properties-common && \
    mkdir -m755 -p /etc/apt/keyrings && \
    wget -O /etc/apt/keyrings/qgis-archive-keyring.gpg https://download.qgis.org/downloads/qgis-archive-keyring.gpg && \
    echo "deb [signed-by=/etc/apt/keyrings/qgis-archive-keyring.gpg] https://qgis.org/debian bullseye main" > /etc/apt/sources.list.d/qgis.list && \
    apt update && \
    apt install -y qgis qgis-plugin-grass

RUN apt-get install -y grass grass-doc

RUN apt update && \
    apt install -y gnupg software-properties-common && \
    apt install -y flatpak gnome-software-plugin-flatpak && \
    flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo && \
    flatpak install -y flathub org.cloudcompare.CloudCompare

RUN apt-get update && apt-get install -y openmpi-bin wget  && \
    mkdir swatplus && \
    cd swatplus && \
    wget https://plus.swat.tamu.edu/downloads/2.3/2.3.1/swatplus-linux-installer-2.3.1.tgz && \
    tar -zxvf swatplus-linux-installer-2.3.1.tgz && \
    /bin/bash installforall.sh && \
    rm swatplus-linux-installer-2.3.1.tgz

RUN conda create -n R-env  r-base r-essentials r-devtools -y  && \
    /bin/bash -c "source activate R-env && \
    R -e \"options(repos = list(CRAN = 'https://cloud.r-project.org/'))\" && \
    R -e \"devtools::install_github('IRkernel/IRkernel')\" && \
    R -e \"IRkernel::installspec(user = FALSE)\"" 

RUN echo "exec /bin/bash" >> /etc/profile
USER jovyan

