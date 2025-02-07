FROM harbor1.fisgeo.unipg.it/uninuvola/base:latest

USER root 

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    bash miniconda.sh -b -p /opt/conda && \
    rm miniconda.sh

ENV PATH="/opt/conda/bin:${PATH}"
ENV JUPYTER_PATH="/usr/local/share/jupyter/kernels"

RUN  conda config --set channel_priority strict && \
     conda create -c conda-forge --name CERN-root root && \
     conda init && \
    /opt/conda/bin/conda shell.bash activate CERN-root && \
    /opt/conda/envs/CERN-root/bin/pip install ipykernel pandas numpy scikit-learn scipy seaborn matplotlib  && \
    /opt/conda/envs/CERN-root/bin/python -m ipykernel install --name CERN-root --display-name CERN-root && \
    /opt/conda/bin/conda shell.bash deactivate




RUN echo "/opt/conda/bin/conda init > /dev/null " >> /etc/profile.d/conda.sh && \
    echo "exec /bin/bash" >> /etc/profile

USER jovyan

