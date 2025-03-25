ARG GIT_BRANCH

FROM harbor1.fisgeo.unipg.it/uninuvola/base:${GIT_BRANCH}

USER root 

# Add the repository
RUN curl https://dl.openfoam.com/add-debian-repo.sh | bash

# Update the repository information
RUN apt-get update && \ 
    apt-get install -y vim  openfoam2312-default paraview htop

RUN echo "exec /bin/bash" >> /etc/profile


USER jovyan
