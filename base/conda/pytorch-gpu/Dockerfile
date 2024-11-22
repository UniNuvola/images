FROM harbor1.fisgeo.unipg.it/uninuvola/conda:latest

USER root 

RUN conda create -n pytorchgpu pytorch torchvision torchaudio pytorch-cuda=12.4 python=3.11.5 -c pytorch -c nvidia && \
    conda init && \
    /opt/conda/bin/conda shell.bash activate pytorchgpu && \
    /opt/conda/envs/pytorchgpu/bin/pip install ipykernel pandas scikit-learn scipy seaborn matplotlib && \
    /opt/conda/envs/pytorchgpu/bin/pip install gymnasium pygame && \
    /opt/conda/envs/pytorchgpu/bin/python -m ipykernel install --name  pytorchgpu --display-name pytorchgpu && \
    /opt/conda/bin/conda shell.bash deactivate


WORKDIR /app
RUN apt update && apt install -y fuse libfuse2 && \
    wget https://github.com/Syllo/nvtop/releases/download/3.1.0/nvtop-x86_64.AppImage && \
    chmod u+x  nvtop-x86_64.AppImage  && ./nvtop-x86_64.AppImage --appimage-extract && \
    ln  /app/squashfs-root/usr/bin/nvtop /usr/local/bin/. &&\
    cp  /app/squashfs-root/usr/lib/*  /usr/local/lib/. &&\
    chmod 755 /usr/local/bin/nvtop

USER jovyan

