FROM ubuntu

RUN apt-get -y update && apt-get -y install python-pip 

RUN pip install Flask

RUN pip install Flask-API

RUN pip install pika

RUN mkdir app
ADD app.py postman.py config.ini app/

CMD python /app/app.py
