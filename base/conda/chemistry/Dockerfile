FROM harbor1.fisgeo.unipg.it/uninuvola/conda:latest

USER root 

RUN conda create -n AmberTools23 -y && \
    conda install -n AmberTools23 -c conda-forge ambertools=23 compilers -y && \
    conda run -n AmberTools23 && conda update -c conda-forge conda -y
RUN /opt/conda/envs/AmberTools23/bin/pip install ipykernel pandas matplotlib numpy
RUN /opt/conda/envs/AmberTools23/bin/python -m ipykernel install --name AmberTools23 --display-name AmberTools23


RUN conda create -n mdtraj -y && \
    conda install -n mdtraj -c conda-forge mdtraj -y && \
    conda run -n mdtraj && conda update -c conda-forge conda -y
RUN /opt/conda/envs/mdtraj/bin/pip install ipykernel pandas matplotlib numpy
RUN /opt/conda/envs/mdtraj/bin/python -m ipykernel install --name mdtraj --display-name mdtraj

ENV FFLAGS="-fallow-argument-mismatch -O3 -mtune=native"

RUN apt-get install -y openmpi-bin libopenmpi-dev
RUN apt-get install -y gfortran mpich cmake xz-utils

WORKDIR /app
RUN mkdir dlpoly
RUN git clone https://gitlab.com/ccp5/dl-poly.git /app/dlpoly/.
WORKDIR /app/dlpoly
RUN mkdir build-pure-mpi
WORKDIR build-pure-mpi
RUN cmake /app/dlpoly/.   -L
RUN cmake /app/dlpoly/build-pure-mpi #-DBUILD_TESTING=ON
RUN make -j16
#ENV PATH="${PATH}:/app/dlpoly/build-pure-mpi"

USER jovyan

