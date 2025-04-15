ARG GIT_BRANCH

FROM harbor1.fisgeo.unipg.it/uninuvola/basedev:${GIT_BRANCH}

USER root

# BondMachine
RUN export BONDMACHINE_DIR=/usr/local/bondmachine && \
    mkdir -p $BONDMACHINE_DIR && \
    curl -fsSL https://www.bondmachine.it/installer/install | bash && \
    chmod -R a+xr $BONDMACHINE_DIR/*

RUN echo "export PATH=\$PATH:/usr/local/bondmachine" > /etc/profile.d/bondmachine.sh

USER jovyan
