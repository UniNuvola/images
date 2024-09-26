FROM harbor1.fisgeo.unipg.it/uninuvola/conda:latest

USER root 

RUN conda create -n pytorch pytorch python=3.11.5
RUN conda init

RUN /opt/conda/bin/conda shell.bash activate  pytorch
RUN /opt/conda/envs/pytorch/bin/pip install ipykernel pandas numpy scikit-learn scipy seaborn matplotlib  
RUN /opt/conda/envs/pytorch/bin/pip install gymnasium matplotlib pygame  
RUN /opt/conda/envs/pytorch/bin/python -m ipykernel install --name  pytorch  --display-name pytorch
RUN /opt/conda/bin/conda shell.bash deactivate

USER jovyan

