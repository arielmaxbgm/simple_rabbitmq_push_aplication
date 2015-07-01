FROM ubuntu

RUN apt-get -y update && apt-get -y install python-pip 

RUN sudo pip install virtualenv

RUN pip install Flask

RUN pip install pika

ADD app.py /home/
