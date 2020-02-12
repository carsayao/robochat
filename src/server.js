'use strict';


var express = require('express');
var socket = require('socket.io');
var assert = require('assert');
const path = require('path');
const { spawn } = require('child_process');
const port = 8080;

var server = express();

server.use('/', express.static(__dirname + '/'));

// var io = socket(server.listen(process.env.PORT || "8080"));
var io = socket(server.listen(port,
  () => console.log(`Listening on port ${port}!`)
));

var start = Date.now();

// Timestamp for debug
function getTime() {
  return (Date.now() - start) / 1000;
};

server.get('/', (req, res) => {
  // res.status(302);
  // res.set({ 'content-type': 'text/plain' });
  // res.redirect('/client.html');

  res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(objectSocket) {
  // console.log('connection!');
  console.log(getTime(), 'connection!');

  io.emit('message', {
    'username': "Welcome message",
    // 'text': "Welcome to my chatroom!"
    'text': "Welcome to my chatroom! Due to issues with the Google App Engine, this website is still under construction."
  });

  objectSocket.on('message', function(objectData) {

    // console.log('objectData',objectData.strQuery);
    // console.log('objectData.strWho', objectData.strWho);
    // console.log('objectData.strQuery', objectData.strQuery);
    console.log(getTime(), 'objectData.strWho', objectData.strWho);
    console.log(getTime(), 'objectData.strQuery', objectData.strQuery);

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
      // console.log("dat",dat);
      console.log(getTime(), typeof dat, "dat", dat);
      var time = getTime();
      io.emit('message', dat);
    });
    subprocess.stderr.on('data', function(data) {
      // console.log(`error:${data}`);
      console.log(getTime(), `error:${data}`);
      io.emit('message', {
        'strWho': "python failed on 'data'",
        'strQuery': ""
      });
    });
    subprocess.stderr.on('close', function() {
      // console.log("Closed");
      console.log(getTime(), "Closed");
    });
  });

  objectSocket.on('clientDisconnect', function() {
    // console.log('disconnection!');
    console.log(getTime(), 'disconnection!');
    io.emit('clientDisconnect');
    start = Date.now();
  });

});

