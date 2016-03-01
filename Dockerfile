FROM python:2.7
RUN apt-get update
#RUN apt-get -y upgrade
#RUN apt-get install -y build-essential python-dev python2.7-dev
RUN apt-get install sqlite3 libsqlite3-dev; exit 0
RUN mkdir /code
ADD . /code
WORKDIR /code
RUN cd /code
RUN pip install -r requirements.txt
CMD python run.py
