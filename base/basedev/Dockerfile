ARG GIT_BRANCH

FROM harbor1.fisgeo.unipg.it/uninuvola/base:${GIT_BRANCH}

USER root

RUN apt update && \
    apt install -y zip unzip unrar-free openssh-client htop procps nano less tmux screen vim curl git gfortran cmake build-essential pkg-config
    
RUN echo "if [ -d /home/jovyan/uniapps/matlab/R2024b ]" > /etc/profile.d/matlab.sh && \
	echo "then" >> /etc/profile.d/matlab.sh && \
	echo "export PATH=/home/jovyan/uniapps/matlab/R2024b/bin:\$PATH" >> /etc/profile.d/matlab.sh && \
	echo "fi" >> /etc/profile.d/matlab.sh

RUN echo "if [ -f /home/jovyan/uniapps/intel/setvars.sh ]" > /etc/profile.d/intel.sh && \
	echo "then" >> /etc/profile.d/intel.sh && \
	echo "source /home/jovyan/uniapps/intel/setvars.sh" >> /etc/profile.d/intel.sh && \
	echo "fi" >> /etc/profile.d/intel.sh

RUN echo "if [ -d /home/jovyan/uniapps/nvidiahpc/Linux_x86_64 ]" > /etc/profile.d/nvidiahpc.sh && \
	echo "then" >> /etc/profile.d/nvidiahpc.sh && \
	echo "export PATH=/home/jovyan/uniapps/nvidiahpc/Linux_x86_64/25.3/compilers/bin:\$PATH" >> /etc/profile.d/nvidiahpc.sh && \
	echo "export MANPATH=/home/jovyan/uniapps/nvidiahpc/Linux_x86_64/25.3/compilers/man:\$MANPATH" >> /etc/profile.d/nvidiahpc.sh && \
	echo "export PATH=/home/jovyan/uniapps/nvidiahpc/Linux_x86_64/25.3/comm_libs/mpi/bin:\$PATH" >> /etc/profile.d/nvidiahpc.sh && \
	echo "fi" >> /etc/profile.d/nvidiahpc.sh

USER jovyan
