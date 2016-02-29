FROM python:2.7
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y build-essential python-dev python2.7-dev
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python run.py

