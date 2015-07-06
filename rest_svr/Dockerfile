FROM ubuntu

RUN apt-get -y update && apt-get -y install python-pip 

RUN pip install Flask

RUN pip install Flask-API

RUN pip install pika

ADD app.py /home/

CMD python /home/app.py
