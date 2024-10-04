FROM harbor1.fisgeo.unipg.it/uninuvola/conda:latest


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

RUN conda create -n  cgat python=3.8.13 -y && conda clean -a -y
RUN conda install -n cgat -c conda-forge -c bioconda \
    _libgcc_mutex=0.1=conda_forge     _openmp_mutex=4.5=2_gnu  aiohttp=3.8.1=py38h0a891b7_1 \
    aiosignal=1.2.0=pyhd8ed1ab_0     alignlib-lite=0.3=py38h9b08285_4     apsw=3.37.0.r1=py38he41bca5_0 \
    async-timeout=4.0.2=pyhd8ed1ab_0     attrs=21.4.0=pyhd8ed1ab_0     bcrypt=3.2.2=py38h0a891b7_0 \
    bedtools=2.30.0=h468198e_3     biopython=1.79=py38h497a2fe_1     boto3=1.23.10=pyhd8ed1ab_0 \
    botocore=1.26.10=pyhd8ed1ab_0     brotli=1.0.9=h166bdaf_7     brotli-bin=1.0.9=h166bdaf_7 \
    brotlipy=0.7.0=py38h0a891b7_1004     bzip2=1.0.8=h7f98852_4     c-ares=1.18.1=h7f98852_0 \
    ca-certificates=2022.5.18.1=ha878542_0     cachetools=5.0.0=pyhd8ed1ab_0    certifi=2022.5.18.1=py38h578d9bd_0 \
    cffi=1.15.0=py38h3931269_0     cgat-apps=0.6.5=py38h1c8579b_2     cgatcore=0.6.14=pyhdfd78af_0 \
    charset-normalizer=2.0.12=pyhd8ed1ab_0      cryptography=37.0.2=py38h2b5fc30_0 \
    cycler=0.11.0=pyhd8ed1ab_0     drmaa=0.7.9=py_1000     fonttools=4.33.3=py38h0a891b7_0 \
    freetype=2.10.4=h0708190_1     frozenlist=1.3.0=py38h0a891b7_1     ftputil=5.0.4=pyhd8ed1ab_0 \
    future=0.18.2=py38h578d9bd_5     gevent=21.12.0=py38h0a891b7_1     giflib=5.2.1=h36c2ea0_2 \
    google-api-core=2.8.1=pyhd8ed1ab_0     google-auth=2.6.6=pyh6c4a22f_0     google-cloud-core=2.2.2=pyh6c4a22f_0 \
    google-cloud-sdk=387.0.0=py38h578d9bd_0     google-cloud-storage=2.1.0=pyh6c4a22f_0     google-crc32c=1.1.2=py38h57c428a_3 \
    google-resumable-media=2.1.0=pyh6c4a22f_0     googleapis-common-protos=1.56.2=py38h578d9bd_0     greenlet=1.1.2=py38hfa26641_2 \
    grpcio=1.46.3=py38ha0cdfde_0     htslib=1.14=h9753748_2     idna=3.3=pyhd8ed1ab_0 \
    jinja2=3.1.2=pyhd8ed1ab_0     jmespath=1.0.0=pyhd8ed1ab_0     joblib=1.1.0=pyhd8ed1ab_0     jpeg=9e=h166bdaf_1 \
    keyutils=1.6.1=h166bdaf_0     kiwisolver=1.4.2=py38h43d8883_1     krb5=1.19.3=h3790be6_0     lcms2=2.12=hddcbb42_0 \
    ld_impl_linux-64=2.36.1=hea4e1c9_2     lerc=3.0=h9c3ff4c_0     libblas=3.9.0=14_linux64_openblas \
    libbrotlicommon=1.0.9=h166bdaf_7     libbrotlidec=1.0.9=h166bdaf_7     libbrotlienc=1.0.9=h166bdaf_7 \
    libcblas=3.9.0=14_linux64_openblas     libcrc32c=1.1.2=h9c3ff4c_0     libcurl=7.83.1=h7bff187_0 \
    libdeflate=1.10=h7f98852_0     libedit=3.1.20191231=he28a2e2_2     libev=4.33=h516909a_1     libffi=3.4.2=h7f98852_5 \
    libgcc=7.2.0=h69d50b8_2     libgcc-ng=12.1.0=h8d9b700_16     libgfortran-ng=12.1.0=h69a702a_16 \
    libgfortran5=12.1.0=hdcd56e2_16     libgomp=12.1.0=h8d9b700_16     liblapack=3.9.0=14_linux64_openblas \
    libnghttp2=1.47.0=h727a467_0     libnsl=2.0.0=h7f98852_0     libopenblas=0.3.20=pthreads_h78a6416_0 \
    libpng=1.6.37=h21135ba_2     libprotobuf=3.20.1=h6239696_0     libsodium=1.0.18=h36c2ea0_1 \
    libssh2=1.10.0=ha56f1ee_2     libstdcxx-ng=12.1.0=ha89aaad_16     libtiff=4.4.0=h0fcbabc_0 \
    libuuid=2.32.1=h7f98852_1000     libuv=1.43.0=h7f98852_0     libwebp=1.2.2=h3452ae3_0     libwebp-base=1.2.2=h7f98852_1 \
    libxcb=1.13=h7f98852_1004     libzlib=1.2.12=h166bdaf_0     lz4-c=1.9.3=h9c3ff4c_1      markupsafe=2.1.1=py38h0a891b7_1 \
    matplotlib-base=3.5.2=py38h826bfd8_0     multidict=6.0.2=py38h0a891b7_1 \
    ncurses=6.3=h27087fc_1     nomkl=1.0=h5ca1d4c_0     numpy=1.22.4=py38h99721a1_0 \
    openssl=1.1.1o=h166bdaf_0     packaging=21.3=pyhd8ed1ab_0     pandas=1.4.2=py38h47df419_2     paramiko=2.11.0=pyhd8ed1ab_0 \
    pcre=8.45=h9c3ff4c_0     pillow=9.1.1=py38h0ee0e06_1     pip=22.1.1=pyhd8ed1ab_0     protobuf=3.20.1=py38hfa26641_0 \
    pthread-stubs=0.4=h36c2ea0_1001     pyasn1=0.4.8=py_0     pyasn1-modules=0.2.7=py_0     pybedtools=0.9.0=py38hf4f3596_1 \
    pybigwig=0.3.18=py38hf8a4f86_2     pycparser=2.21=pyhd8ed1ab_0     pynacl=1.5.0=py38h0a891b7_1 \
    pyopenssl=22.0.0=pyhd8ed1ab_0     pyparsing=3.0.9=pyhd8ed1ab_0     pysam=0.19.1=py38h8bf8b8d_0     pysftp=0.2.9=py_1 \
    pysocks=1.7.1=py38h578d9bd_5     python=3.8.13=h582c2e5_0_cpython     python-dateutil=2.8.2=pyhd8ed1ab_0 \
    python_abi=3.8=2_cp38     pytz=2022.1=pyhd8ed1ab_0     pyu2f=0.1.5=pyhd8ed1ab_0     pyyaml=6.0=py38h0a891b7_4 \
    quicksect=0.2.2=py38hbff2b2d_5     readline=8.1=h46c0cb4_0     requests=2.27.1=pyhd8ed1ab_0     rsa=4.8=pyhd8ed1ab_0 \
    ruffus=2.8.4=pyh864c0ab_1     s3transfer=0.5.2=pyhd8ed1ab_0     scikit-learn=1.1.1=py38hf80bbf7_0 \
    scipy=1.8.1=py38h1ee437e_0   setuptools=62.3.2=py38h578d9bd_0     six=1.16.0=pyh6c4a22f_0     sortedcontainers=2.4.0=pyhd8ed1ab_0 \
    sqlalchemy=1.4.36=py38h0a891b7_0     sqlite=3.38.5=h4ff8645_0     threadpoolctl=3.1.0=pyh8a188c0_0     time=1.8=h516909a_0   \
    tk=8.6.12=h27826a3_0  typing-extensions=4.2.0=hd8ed1ab_1     typing_extensions=4.2.0=pyha770c72_1     ucsc-bedgraphtobigwig=357=0 \
    ucsc-bedtobigbed=357=0     ucsc-wigtobigwig=357=0   unicodedata2=14.0.0=py38h0a891b7_1     urllib3=1.26.9=pyhd8ed1ab_0 \
    wheel=0.37.1=pyhd8ed1ab_0     xorg-libxau=1.0.9=h7f98852_0     xorg-libxdmcp=1.1.3=h7f98852_0     xz=5.2.5=h516909a_1 \
    yaml=0.2.5=h7f98852_2     yarl=1.7.2=py38h0a891b7_2     zlib=1.2.12=h166bdaf_0 \
    zope.event=4.5.0=pyh9f0ad1d_0     zope.interface=5.4.0=py38h0a891b7_2     zstd=1.5.2=h8a70e8d_1 \
    && conda clean -a -y
RUN /opt/conda/envs/cgat/bin/pip install ipykernel
RUN /opt/conda/envs/cgat/bin/python -m ipykernel install --name cgat --display-name cgat

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
    mv /app/STAR/bin/Linux_x86_64/STAR /usr/local/bin/.
    mv /app/beagle.jar /usr/ocal/bin/.
RUN echo "exec /bin/bash" >> /etc/profile

USER jovyan



