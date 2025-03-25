FROM harbor1.fisgeo.unipg.it/uninuvola/conda:latest

USER root 


RUN apt-get update && \
    apt-get install -y openmpi-bin libopenmpi-dev

RUN conda create -n tensorflow tensorflow scikit-learn python=3.11.5 && \
    conda init && \
    /opt/conda/bin/conda shell.bash activate  tensorflow && \
    /opt/conda/envs/tensorflow/bin/pip install numpy matplotlib pandas keras ipykernel && \
    /opt/conda/envs/tensorflow/bin/python -m ipykernel install --name  tensorflow  --display-name tensorflow # && \
    # /opt/conda/bin/conda  install -c conda-forge

RUN echo "/opt/conda/bin/conda init > /dev/null " >> /etc/profile.d/conda.sh && \
    echo "exec /bin/bash" >> /etc/profile

USER jovyan

