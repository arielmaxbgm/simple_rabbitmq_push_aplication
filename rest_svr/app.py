# Demo application that notify a message coming from REST API to a message bus (rabbitmq)

from flask.ext.api import FlaskAPI, status
from flask import request
from ConfigParser import ConfigParser
import pika

app = FlaskAPI(__name__)

# Msg bus configuration
config = ConfigParser()
config.read('config.ini')
msg_bus = config.get('General','msg_bus_host')
msg_bus_port = config.get('General', 'msg_bus_port')
queue = config.get('General', 'msg_bus_queue')

# Send a message to the message bus (rabbitmq)
def send_message(message):
	connection = pika.BlockingConnection(pika.ConnectionParameters(host=msg_bus, port=msg_bus_port))
	channel = connection.channel()
	channel.queue_declare(queue='hello')
	channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=msg.str())
	connection.close()

@app.route('/notify', methods=['POST'])
def notify():
	msg = request.form['msg']
	send_message(msg)
	return '', status.HTTP_201_CREATED

if __name__ == '__main__':
    app.run(host='0.0.0.0')
