FROM python:3.9
# ENV

RUN mkdir -p /home/app

WORKDIR /home/app

COPY squareNumbers.py  /home/app
COPY requirements.txt  /home/app

RUN  pip3 install -r requirements.txt

CMD [ "python", "/home/app/squareNumbers.py"]


