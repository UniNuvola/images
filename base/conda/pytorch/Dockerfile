FROM harbor1.fisgeo.unipg.it/uninuvola/conda:latest

USER root 

RUN conda create -n pytorch pytorch python=3.11.5 && \
    conda init && \
    /opt/conda/bin/conda shell.bash activate  pytorch && \
    /opt/conda/envs/pytorch/bin/pip install ipykernel pandas numpy scikit-learn scipy seaborn matplotlib && \
    /opt/conda/envs/pytorch/bin/pip install gymnasium pygame && \
    /opt/conda/envs/pytorch/bin/python -m ipykernel install --name  pytorch --display-name pytorch && \
    /opt/conda/bin/conda shell.bash deactivate


RUN echo "exec /bin/bash" >> /etc/profile

USER jovyan

