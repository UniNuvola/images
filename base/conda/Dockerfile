ARG GIT_BRANCH

FROM harbor1.fisgeo.unipg.it/uninuvola/base:${GIT_BRANCH}

USER root 

ENV PATH="/opt/conda/bin:${PATH}"
ENV JUPYTER_PATH="/usr/local/share/jupyter/kernels"

RUN echo "/opt/conda/bin/conda init > /dev/null " >> /etc/profile.d/conda.sh

USER jovyan

