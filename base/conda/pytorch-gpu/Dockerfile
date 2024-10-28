FROM harbor1.fisgeo.unipg.it/uninuvola/conda:latest

USER root 

RUN conda create -n pytorchgpu pytorch torchvision torchaudio pytorch-cuda=12.4 nvtop python=3.11.5 -c pytorch -c nvidia && \
    conda init && \
    /opt/conda/bin/conda shell.bash activate pytorchgpu && \
    /opt/conda/envs/pytorchgpu/bin/pip install ipykernel pandas scikit-learn scipy seaborn matplotlib && \
    /opt/conda/envs/pytorchgpu/bin/pip install gymnasium pygame && \
    /opt/conda/envs/pytorchgpu/bin/python -m ipykernel install --name  pytorchgpu --display-name pytorchgpu && \
    /opt/conda/bin/conda shell.bash deactivate

USER jovyan

