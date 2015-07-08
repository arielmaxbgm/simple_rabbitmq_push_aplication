var amqp = require('amqp');
var json_config = require('./config.json');

console.log(json_config);
var msg_host = json_config.msg_bus_host;
var msg_queue = json_config.msg_bus_queue;

var connection = amqp.createConnection({ host: msg_host });

// Wait for connection to become established.
connection.on('ready', function () {
  // Use the default 'amq.topic' exchange
  connection.queue(msg_queue, { 'passive': true }, function (q) {
      // Catch all messages
      q.bind('#');

      // Receive messages
      q.subscribe(function (message) {
        // Print messages to stdout
        console.log(message.data.toString());
      });
  });
});
