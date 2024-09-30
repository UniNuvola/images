FROM harbor1.fisgeo.unipg.it/uninuvola/conda:latest

USER root 

RUN conda create -n tensorflow tensorflow scikit-learn python=3.11.5
RUN conda init


RUN /opt/conda/bin/conda shell.bash activate  tensorflow
RUN /opt/conda/envs/tensorflow/bin/pip install numpy matplotlib pandas keras ipykernel
RUN /opt/conda/envs/tensorflow/bin/python -m ipykernel install --name  tensorflow  --display-name tensorflow
RUN /opt/conda/bin/conda  install -c conda-forge hdf5=1.10.5

USER jovyan

