FROM harbor1.fisgeo.unipg.it/uninuvola/base:latest

USER root 

# Add the repository
RUN curl https://dl.openfoam.com/add-debian-repo.sh | bash
RUN ls

# Update the repository information
RUN apt-get update

# Install preferred package. Eg,
RUN apt-get install -y vim 
RUN apt-get install -y openfoam2312-default

RUN apt-get install -y paraview
RUN apt-get install -y htop
# Use the openfoam shell session. Eg,
#openfoam2312


USER jovyan
