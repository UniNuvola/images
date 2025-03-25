ARG GIT_BRANCH

FROM harbor1.fisgeo.unipg.it/uninuvola/conda:${GIT_BRANCH}

USER root



RUN conda create -n cplex python=3.11 && \
    conda init && \
    /opt/conda/bin/conda shell.bash activate cplex && \
    /opt/conda/envs/cplex/bin/pip install cplex ipykernel pandas numpy scikit-learn scipy seaborn matplotlib && \
    /opt/conda/envs/cplex/bin/python -m ipykernel install --name  cplex --display-name cplex && \
    /opt/conda/bin/conda shell.bash deactivate




RUN conda create -n gurobipy python=3.12 && \
    conda init && \
    /opt/conda/bin/conda shell.bash activate  gurobipy && \
    /opt/conda/envs/gurobipy/bin/pip install gurobipy ipykernel pandas numpy scikit-learn scipy seaborn matplotlib && \
    /opt/conda/envs/gurobipy/bin/python -m ipykernel install --name  gurobipy --display-name gurobipy && \
    /opt/conda/bin/conda shell.bash deactivate


RUN conda create -n PuLP python=3.12 && \
    conda init && \
    /opt/conda/bin/conda shell.bash activate PuLP && \
    /opt/conda/envs/PuLP/bin/pip install PuLP ipykernel pandas numpy scikit-learn scipy seaborn matplotlib && \
    /opt/conda/envs/PuLP/bin/python -m ipykernel install --name  PuLP --display-name PuLP && \
    /opt/conda/bin/conda shell.bash deactivate

RUN echo "/opt/conda/bin/conda init > /dev/null " >> /etc/profile.d/conda.sh && \
    echo "exec /bin/bash" >> /etc/profile

USER jovyan

