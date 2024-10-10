FROM harbor1.fisgeo.unipg.it/uninuvola/conda:latest

USER root 

RUN conda create -n pytorchgpu python=3.11.5 && \
    conda init && \
    /opt/conda/bin/conda shell.bash activate pytorchgpu && \
    /opt/conda/bin/conda install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia && \
    /opt/conda/envs/pytorchgpu/bin/pip install ipykernel pandas numpy scikit-learn scipy seaborn matplotlib && \
    /opt/conda/envs/pytorchgpu/bin/pip install gymnasium pygame && \
    /opt/conda/envs/pytorchgpu/bin/python -m ipykernel install --name  pytorchgpu --display-name pytorchgpu && \
    /opt/conda/bin/conda shell.bash deactivate

USER jovyan

