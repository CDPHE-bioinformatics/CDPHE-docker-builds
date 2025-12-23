FROM mambaorg/micromamba:2.3.2

LABEL maintainer "Arianna Smith <arianna.smith@state.co.us"
LABEL registry "Docker Hub"
LABEL namespace "ariannaesmith"
LABEL repository "artic-fieldbioinformatics"
LABEL source_code "https://github.com/CDPHE-bioinformatics/CDPHE-docker-builds"

ENV ARTIC_VERSION="v1.8.5"

USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential wget procps && \
    wget https://api.github.com/repos/artic-network/fieldbioinformatics/tarball/${ARTIC_VERSION} -O ${ARTIC_VERSION}.tar.gz && \
    tar -xvzf ${ARTIC_VERSION}.tar.gz && \ 
    rm ${ARTIC_VERSION}.tar.gz && \
    mv ./artic-network-fieldbioinformatics-*/ ./artic-network-fieldbioinformatics && \
    sed -i 's/name: artic/name: base/' ./artic-network-fieldbioinformatics/environment.yml && \
    micromamba install -y -n base -f ./artic-network-fieldbioinformatics/environment.yml && \
    micromamba clean --all --yes
ARG MAMBA_DOCKERFILE_ACTIVATE=1

RUN python3 -m pip install ./artic-network-fieldbioinformatics && \
    artic_get_models

ENTRYPOINT ["/usr/local/bin/_entrypoint.sh"]

CMD ["/bin/bash"]
