'use strict';

var express = require('express');
var socket = require('socket.io');
var assert = require('assert');
const path = require('path');
const { spawn } = require('child_process');

var server = express();

server.use('/', express.static(__dirname + '/'));

var io = socket(server.listen(process.env.PORT || 8080));

server.get('/', (req, res) => {
  // res.status(302);
  // res.set({ 'content-type': 'text/plain' });
  // res.redirect('/client.html');

  res.sendFile(__dirname + '/client.html');
});

io.on('connection', function(objectSocket) {
  console.log('connection!');

  io.emit('message', {
    'username': "Welcome message",
    'text': 'Welcome to my chatroom!'
  });

  objectSocket.on('message', function(objectData) {

    // console.log('objectData',objectData.strQuery);
    console.log('objectData.strWho', objectData.strWho);
    console.log('objectData.strQuery', objectData.strQuery);

    // https://www.tutorialspoint.com/run-python-script-from-node-js-using-child-process-spawn-method
    function getPython() {
      return spawn('python3', [
        // M: unbuffered output
        '-u',
        path.join(__dirname, 'markov.py'),
        objectData.strWho,
        objectData.strQuery
      ]);
    }
    const subprocess = getPython();
    subprocess.stdout.on('data', function(data) {
      var dat = JSON.parse(data.toString());
      console.log("dat",dat);
      io.emit('message', dat);
    });
    subprocess.stderr.on('data', function(data) {
      console.log(`error:${data}`);
    });
    subprocess.stderr.on('close', function() {
      console.log("Closed");
    });
  });

  objectSocket.on('disconnect', function() {
    console.log('disconnection!');
  });

});

