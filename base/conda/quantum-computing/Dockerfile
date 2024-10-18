FROM harbor1.fisgeo.unipg.it/uninuvola/conda:latest

USER root 

RUN conda create -n spinqit python=3.9.12  && \
    conda init && \
    /opt/conda/bin/conda shell.bash activate spinqit && \
    /opt/conda/envs/spinqit/bin/pip install ipykernel && \
    /opt/conda/envs/spinqit/bin/python -m ipykernel install --name  spinqit --display-name spinqit && \
    /opt/conda/envs/spinqit/bin/pip install torch && \
    /opt/conda/envs/spinqit/bin/pip install spinqit && \
    /opt/conda/bin/conda shell.bash deactivate

RUN conda create -n ocean python=3.11.5 && \
    conda init && \
    /opt/conda/bin/conda shell.bash activate ocean && \
    /opt/conda/envs/ocean/bin/pip install ipykernel && \
    /opt/conda/envs/ocean/bin/python -m ipykernel install --name  ocean --display-name ocean && \
    /opt/conda/envs/ocean/bin/pip install dwave-ocean-sdk && \
    /opt/conda/bin/conda shell.bash deactivate

RUN conda create -n  qiskit python=3.11.5 && \
    conda init && \
    /opt/conda/bin/conda shell.bash activate qiskit && \
    /opt/conda/envs/qiskit/bin/pip install ipykernel && \
    /opt/conda/envs/qiskit/bin/python -m ipykernel install --name  qiskit --display-name qiskit && \
    /opt/conda/envs/qiskit/bin/pip install qiskit && \
    /opt/conda/envs/qiskit/bin/pip install qiskit-aer && \
    /opt/conda/envs/qiskit/bin/pip install qiskit_ibm_runtime && \
    /opt/conda/bin/conda shell.bash deactivate

RUN apt install -y nano less tmux screen

RUN echo "exec /bin/bash" >> /etc/profile

USER jovyan

