FROM python:3.10.9

LABEL maintainer "Arianna Smith <arianna.smith@state.co.us>"

WORKDIR /

COPY requirements.txt /

RUN pip3 install -r /requirements.txt

COPY . /

CMD ["/bin/bash"]
