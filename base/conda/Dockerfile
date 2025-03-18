FROM harbor1.fisgeo.unipg.it/uninuvola/base:latest

USER root 

ENV PATH="/opt/conda/bin:${PATH}"
ENV JUPYTER_PATH="/usr/local/share/jupyter/kernels"

RUN echo "/opt/conda/bin/conda init > /dev/null " >> /etc/profile.d/conda.sh && \
    echo "exec /bin/bash" >> /etc/profile

USER jovyan

