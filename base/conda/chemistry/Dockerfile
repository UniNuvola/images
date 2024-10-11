FROM harbor1.fisgeo.unipg.it/uninuvola/conda:latest

USER root 

RUN conda create -n AmberTools23 -y && \
    conda install -n AmberTools23 -c conda-forge ambertools=23 compilers -y && \
    conda run -n AmberTools23 && conda update -c conda-forge conda -y && \
    /opt/conda/envs/AmberTools23/bin/pip install ipykernel pandas matplotlib numpy  && \
    /opt/conda/envs/AmberTools23/bin/python -m ipykernel install --name AmberTools23 --display-name AmberTools23

RUN conda create -n mdtraj -y && \
    conda install -n mdtraj -c conda-forge mdtraj -y && \
    conda run -n mdtraj && conda update -c conda-forge conda -y  && \
    /opt/conda/envs/mdtraj/bin/pip install ipykernel pandas matplotlib numpy  && \
    /opt/conda/envs/mdtraj/bin/python -m ipykernel install --name mdtraj --display-name mdtraj

ENV FFLAGS="-fallow-argument-mismatch -O3 -mtune=native"

# For DLPOLY
RUN apt-get install -y openmpi-bin libopenmpi-dev gfortran mpich cmake xz-utils

WORKDIR /app
RUN mkdir dlpoly && \
    git clone https://gitlab.com/ccp5/dl-poly.git /app/dlpoly/.  && \
    cd /app/dlpoly && \
    mkdir build-pure-mpi  && \
    cd build-pure-mpi  && \
    cmake /app/dlpoly/. -L && \
    cmake /app/dlpoly/build-pure-mpi  && \
    make -j16
#ENV PATH="${PATH}:/app/dlpoly/build-pure-mpi"

USER jovyan

