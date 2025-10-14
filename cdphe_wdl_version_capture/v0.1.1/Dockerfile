FROM python:3.10.12

LABEL base.image="python:3.10.12"
LABEL description="WDL workflow and task version capture"
LABEL maintainer "Arianna Smith <arianna.smith@state.co.us>"

ENV HOST='ariannaesmith'
ENV NAME="cdphe_wdl_version_capture"
ENV VERSION="v0.1.1"
ENV APPDIR=/usr/src/app
ENV PATH="/usr/src/app:$PATH"

WORKDIR $APPDIR


COPY scripts/* ./
COPY requirements.txt ./

RUN pip3 install -r requirements.txt

CMD ["python3", "./test.py"]