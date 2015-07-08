# Demo application that notify a message coming from REST API to a message bus (rabbitmq)

from flask.ext.api import FlaskAPI, status
from flask import request
from postman import Postman
app = FlaskAPI(__name__)

# Msg bus configuration
postman = Postman('app/config.ini')

@app.route('/notify', methods=['POST'])
def notify():
	msg = request.form['msg']
	postman.send_message(msg)
	return '', status.HTTP_201_CREATED

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
