
from ConfigParser import ConfigParser
import pika

# Class that represents a postman message manager
# using pika as rabbitmq client
class Postman:
	def __init__(self, config_file):
		# Msg bus configuration
		self.__config = ConfigParser()
		# if file doesnt exists it load an empty config file
		self.__config.read(config_file)

	# Send a message using pika as rabbitmq client
	def send_message(self, msg):
		msg_bus = self.__config.get('General','msg_bus_host')
		msg_bus_port = self.__config.getint('General', 'msg_bus_port')
		msg_queue = self.__config.get('General', 'msg_bus_queue')
		connection = pika.BlockingConnection(pika.ConnectionParameters(host=msg_bus, port=msg_bus_port))
		channel = connection.channel()
		channel.queue_declare(queue=msg_queue)
		channel.basic_publish(exchange='',
	                      routing_key=msg_queue,
	                      body=msg.str())
		connection.close()

