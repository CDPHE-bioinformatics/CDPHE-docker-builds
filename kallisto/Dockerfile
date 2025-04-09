# Kallisto
# version: v0.51.0

FROM ubuntu:jammy as app

# List all software versions are ARGs near the top of the dockerfile
# 'ARG' sets environment variables during the build stage
# ARG variables are ONLY available during image build, they do not persist in the final image
ARG KALLISTO_VER="0.51.0"

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="0.51.0"
LABEL software="kallisto"
LABEL software.version="${KALLISTO_VER}"
LABEL description="kallisto is a program for quantifying abundances of transcripts from bulk and single-cell RNA-Seq data, or more generally of target sequences using high-throughput sequencing reads."
LABEL website="https://github.com/StaPH-B/docker-builds"
LABEL license="https://github.com/StaPH-B/docker-builds/blob/master/LICENSE"
LABEL maintainer="Molly Hetherington-Rauth"
LABEL maintainer.email="molly.hetheringtonrauth@state.co.us"

# 'RUN' executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends\
    wget \ 
    ca-certificates \ 
    autoconf \
    build-essential \ 
    cmake \ 
    zlib1g-dev \
    libhdf5-dev && \ 
    apt-get autoclean && rm -rf /var/lib/apt/lists/*


# Get source file and compile htslib and kallisto
RUN wget "http://github.com/pachterlab/kallisto/archive/refs/tags/v${KALLISTO_VER}.tar.gz" && \
    tar -xzf v${KALLISTO_VER}.tar.gz && \
    rm -v v${KALLISTO_VER}.tar.gz && \
    cd kallisto-${KALLISTO_VER} && \
    cd ext/htslib && \
    autoheader && \
    autoconf && \
    cd ../.. && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make && \
    make install 


##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####
##### This is fro adding to staphb docker containers
##### Step 2. Set up the testing stage.                                 #####
##### The docker image is built to the 'test' stage before merging, but #####
##### the test stage (or any stage after 'app') will be lost.           #####
##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####

# A second FROM insruction creates a new stage
# FROM app as test

# # set working directory so that all test inputs & outputs are kept in /test
# # copying kallisto test data into wd /test
# RUN mkdir -p /test && cp kallisto-${KALLISTO_VER}/test/* /test/

# WORKDIR /test

# # print help and version info; check dependencies (not all software has these options available)
# # Mostly this ensures the tool of choice is in path and is executable
# RUN kallisto version

# # Run the program's internal tests
# RUN kallisto index -i transcripts.idx transcripts.fasta.gz && \
#     kallisto quant -i transcripts.idx -o output -b 100 reads_1.fastq.gz reads_2.fastq.gz

# # set the new directory because I don't want to be in the test directory
# WORKDIR /data




