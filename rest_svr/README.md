# Docker image with an API Rest using Flask

## Setup
Run setup.sh in order to update the rabbitmq container.

## API REST

| URL  | METHOD  | PARAMETERS |
| :------------ |:---------------:| -----:|
| http://\<host\>:5000/notify      | GET | example { 'msg': 'a message'} |
