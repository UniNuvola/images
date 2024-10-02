FROM harbor1.fisgeo.unipg.it/uninuvola/conda:latest
FROM harbor1.fisgeo.unipg.it/uninuvola/cgat-env:latest

USER root 
RUN apt-get update
RUN apt-get install -y openssh-server htop
RUN apt-get install -y vim hwloc wget  libncurses-dev
RUN apt-get install -y openmpi-bin libopenmpi-dev gfortran mpich cmake xz-utils
RUN apt-get install -y libbz2-dev liblzma-dev libncurses-dev
RUN apt install -y openjdk-17-jre-headless unzip libboost-all-dev gawk bison r-base libgsl0-dev
RUN apt-get install -y libpq-dev python-dev-is-python3
RUN apt install -y nano less tmux screen

RUN conda config --add channels bioconda
RUN conda config --add channels conda-forge
RUN conda config --set channel_priority strict

RUN conda create -n  genomics-capomaccio cutadapt
RUN /opt/conda/bin/conda shell.bash activate  genomics-capomaccio
RUN /opt/conda/envs/genomics-capomaccio/bin/pip install ipykernel bowtie biopython agat matplotlib  pandas matplotlib numpy pysam Cython psycopg2-binary
RUN /opt/conda/envs/genomics-capomaccio/bin/python -m ipykernel install --name genomics-capomaccio --display-name genomics-capomaccio
RUN /opt/conda/bin/conda shell.bash deactivate

RUN conda create -n genomics-lasagna -c bioconda -c conda-forge salmon gemma snpeff && \
    conda clean -a
RUN /opt/conda/bin/conda shell.bash activate  genomics-lasagna
RUN /opt/conda/envs/genomics-lasagna/bin/pip install ipykernel pandas matplotlib numpy
RUN /opt/conda/envs/genomics-lasagna/bin/python -m ipykernel install --name genomics-lasagna --display-name genomics-lasagna
RUN /opt/conda/bin/conda shell.bash deactivate

RUN conda create -n R-env  r-base r-essentials r-devtools -y
RUN /bin/bash -c "source activate R-env && \
    R -e \"options(repos = list(CRAN = 'https://cloud.r-project.org/'))\" && \
    R -e \"devtools::install_github('IRkernel/IRkernel')\" && \
    R -e \"IRkernel::installspec(user = FALSE)\""
RUN /bin/bash -c "source activate R-env && R -e 'install.packages(\"lfmm\", repos=\"http://cran.us.r-project.org\")'"

WORKDIR /app
#GNU PARALLEL all fatto
RUN wget http://ftp.gnu.org/gnu/parallel/parallel-latest.tar.bz2 && \
    tar xjf parallel-latest.tar.bz2

### BEDTOOLS all fatto
RUN wget https://github.com/arq5x/bedtools2/releases/download/v2.29.1/bedtools-2.29.1.tar.gz && \
    tar -zxvf bedtools-2.29.1.tar.gz

# GFFREAD 1
RUN git clone https://github.com/gpertea/gffread

#SEQTK 1
RUN git clone https://github.com/lh3/seqtk.git

#PICARD 1
RUN git clone https://github.com/broadinstitute/picard.git

## TRIMGALORE 
RUN curl -fsSL https://github.com/FelixKrueger/TrimGalore/archive/0.6.10.tar.gz -o trim_galore.tar.gz &&  \
    tar xvzf trim_galore.tar.gz

## VCFTOOLS 1
RUN git clone https://github.com/vcftools/vcftools.git

#STAR  3
RUN git clone https://github.com/alexdobin/STAR.git

#FEATURECOUNTS
RUN wget https://sourceforge.net/projects/subread/files/subread-2.0.7/subread-2.0.7-source.tar.gz
RUN tar -zxvf subread-2.0.7-source.tar.gz && cd /app/subread-2.0.7-source/src && make -f Makefile.Linux

WORKDIR /app/parallel-20240922/
RUN ./configure && make &&  make install
WORKDIR  /app/bedtools2
RUN make
WORKDIR /app/gffread
RUN make release
WORKDIR /app/seqtk
RUN  make
WORKDIR /app/picard/
RUN ./gradlew shadowJar
WORKDIR /app/vcftools/
RUN ./autogen.sh && ./configure && make && make install
WORKDIR /app/STAR/source
RUN make STAR


WORKDIR /app
RUN rm *.tar.gz *.zip

WORKDIR /usr/local/bin
RUN wget https://faculty.washington.edu/browning/beagle/beagle.06Aug24.a91.jar -O beagle.jar

RUN mv /app/TrimGalore-0.6.10/trim_galore /usr/local/bin/. && \
    mv /app/bedtools2/bin/* /usr/local/bin/. && \
    mv /app/STAR/bin/Linux_x86_64/STAR /usr/local/bin/. && \
    mv /app/beagle.jar /usr/ocal/bin/.
RUN echo "exec /bin/bash" >> /etc/profile

USER jovyan



