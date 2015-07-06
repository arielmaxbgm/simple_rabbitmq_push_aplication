# Demo application that notify a message coming from REST API to a message bus (rabbitmq)

from flask.ext.api import FlaskAPI, status
from flask import request
import pika

app = FlaskAPI(__name__)
msg_bus = '172.17.0.13'
msg_bus_port = 9672
@app.route('/notify', methods=['POST'])
def notify():
	msg = request.form['msg']
	connection = pika.BlockingConnection(pika.ConnectionParameters(host=msg_bus, port=msg_bus_port))
	channel = connection.channel()
	channel.queue_declare(queue='hello')
	channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=msg.str())
	print " [x] Sent " + msg.str() + " to " + msg_bus
	return '', status.HTTP_201_CREATED

connection.close()
    return request.form['suscriptor'] 

if __name__ == '__main__':
    app.run(host='0.0.0.0')
