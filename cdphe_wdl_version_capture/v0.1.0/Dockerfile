FROM python:3.7

LABEL base.image="python:3.7"
LABEL description="WDL workflow and task version capture"
LABEL host='ariannaesmith'
LABEL name="cdphe_wdl_version_capture"
LABEL dockerfile.version="v0.1.0"
LABEL maintainer "Arianna Smith <arianna.smith@state.co.us>"

WORKDIR /usr/src/app

ENV PATH="/usr/src/app:$PATH"

COPY scripts/* ./
COPY requirements.txt ./

RUN pip3 install -r requirements.txt
