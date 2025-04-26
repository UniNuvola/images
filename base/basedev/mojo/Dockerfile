ARG GIT_BRANCH

FROM harbor1.fisgeo.unipg.it/uninuvola/basedev:${GIT_BRANCH}

USER root

# Mojo
RUN export MODULAR_HOME=/usr/local/modular && \
    curl -ssL https://magic.modular.com/deb19838-0fd0-4434-ae16-2dafdf74efde | bash && \
    /usr/local/modular/bin/magic global install max-pipelines

RUN echo "export PATH=\$PATH:/usr/local/modular/bin" > /etc/profile.d/modular.sh

USER jovyan
