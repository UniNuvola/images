FROM harbor1.fisgeo.unipg.it/uninuvola/conda:latest

USER root 

RUN conda create -n tensorflow tensorflow scikit-learn python=3.11.5 && \
    conda init && \
    /opt/conda/bin/conda shell.bash activate  tensorflow && \
    /opt/conda/envs/tensorflow/bin/pip install numpy matplotlib pandas keras ipykernel && \
    /opt/conda/envs/tensorflow/bin/python -m ipykernel install --name  tensorflow  --display-name tensorflow && \
    /opt/conda/bin/conda  install -c conda-forge hdf5=1.10.5 

RUN echo "exec /bin/bash" >> /etc/profile

USER jovyan

