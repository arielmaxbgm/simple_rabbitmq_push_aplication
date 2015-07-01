FROM ubuntu

RUN apt-get -y update && apt-get -y install wget

# Install instructions: https://www.rabbitmq.com/install-debian.html
RUN wget https://www.rabbitmq.com/rabbitmq-signing-key-public.asc

RUN apt-key add rabbitmq-signing-key-public.asc

RUN apt-get -y install rabbitmq-server
