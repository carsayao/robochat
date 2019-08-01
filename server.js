'use strict';

var express = require('express'); // do not change this line
var socket = require('socket.io'); // do not change this line
var assert = require('assert'); // do not change this line
const path = require('path');
const { spawn } = require('child_process');

var server = express();

server.use('/', express.static(__dirname + '/'));

var io = socket(server.listen(process.env.PORT || 8080)); // do not change this line

var message;

io.on('connection', (objectSocket) => {
  console.log('connection!');

  objectSocket.on('message', (objectData) => {
    // https://www.tutorialspoint.com/run-python-script-from-node-js-using-child-process-spawn-method
    function runScript() {
      return spawn('python3', [
        // M: unbuffered output
        // '-u',
        path.join(__dirname, 'markov.py')
      ]);
    }
    const subprocess = runScript();
    subprocess.stdout.on('data', (data) => {
      console.log('server data', data);
      message = `${data}`;
      console.log('server message', message);
      console.log('stdout', `data:${data}`);
    });
    console.log('1');
    subprocess.stderr.on('data', (data) => {
      console.log(`error:${data}`);
    });
    console.log('2');
    subprocess.stderr.on('close', () => {
      console.log("Closed");
    });
    console.log('3');

    // assert(message !== undefined);
    // M: emit the message. for some reason i reach this point before message has been set. may have to do with buffered/unbuffered output. maybe try a promise.
    if (message !== undefined) {
      // M: getting a string (message)
      console.log('server message', message);
      objectSocket.emit('message', message);
    }

  });

  objectSocket.on('disconnect', () => {
    console.log('disconnection!');
  });

});

/*
// https://stackoverflow.com/questions/20828755/returning-data-from-python-to-node-js#20862218
// var str;
var util = require('util'),
  spawn = require('child_process').spawn,
  dummy = spawn('python3', ['markov.py']);

io.on('connection', function (objectSocket) {
  console.log('connection!');
  objectSocket.on('message', () => {

    console.log('message');
    dummy.stdout.on('data', (data) => {
      // util.print(data.toString());
      // console.log(data.toString());
      console.log('data',data);
    });
    // console.log(str)

  });


  objectSocket.on('disconnect', () => {
    console.log('disconnection!');
  });


});
*/