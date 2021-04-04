FROM python:3.9

# Instal what you need
# RUN python3 -m pip install numpy

RUN mkdir -p /pipelines/component/src 

WORKDIR /pipelines/component/src

COPY program.py /pipelines/component/src
COPY requirements.txt /pipelines/component/src

RUN  pip3 install -r requirements.txt

