from ubuntu

RUN apt-get -y install software-properties-common

RUN add-apt-repository ppa:chris-lea/node.js

RUN apt-get update 

RUN apt-get install -y nodejs

RUN apt-get install -y build-essential

RUN npm install amqp

ADD suscriber.js /home/suscriber.js

CMD node /home/suscriber.js
