FROM harbor1.fisgeo.unipg.it/uninuvola/conda:latest

USER root 

RUN conda create -n spinqit python=3.9.12
RUN conda init
RUN /opt/conda/bin/conda shell.bash activate spinqit
RUN /opt/conda/envs/spinqit/bin/pip install ipykernel
RUN /opt/conda/envs/spinqit/bin/python -m ipykernel install --name  spinqit      --display-name spinqit
RUN /opt/conda/envs/spinqit/bin/pip install torch
RUN /opt/conda/envs/spinqit/bin/pip install spinqit
RUN /opt/conda/bin/conda shell.bash deactivate

RUN conda create -n ocean python=3.11.5
RUN conda init
RUN /opt/conda/bin/conda shell.bash activate ocean
RUN /opt/conda/envs/ocean/bin/pip install ipykernel
RUN /opt/conda/envs/ocean/bin/python -m ipykernel install --name  ocean --display-name ocean
RUN /opt/conda/envs/ocean/bin/pip install dwave-ocean-sdk
RUN /opt/conda/bin/conda shell.bash deactivate

RUN conda create -n  qiskit python=3.11.5
RUN conda init
RUN /opt/conda/bin/conda shell.bash activate qiskit
RUN /opt/conda/envs/qiskit/bin/pip install ipykernel
RUN /opt/conda/envs/qiskit/bin/python -m ipykernel install --name  qiskit --display-name qiskit
RUN /opt/conda/envs/qiskit/bin/pip install qiskit
RUN /opt/conda/envs/qiskit/bin/pip install qiskit-aer
RUN /opt/conda/envs/qiskit/bin/pip install qiskit_ibm_runtime
RUN /opt/conda/bin/conda shell.bash deactivate

USER jovyan

