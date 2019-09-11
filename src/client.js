// Unused


var objectSocket = io.connect('http://localhost:8080/');

objectSocket.on('message', function (objectData) {
  console.log('client objectData', objectData);
  $('#output')
    .prepend('> ' + objectData.text + '\n\n')
    ;
});

$('#submit')
  .on('click', function () {
    console.log('who', $("input[type='radio']:checked").attr('id'));
    console.log('message', $('#message').val());
    objectSocket.emit('message', {
      'strWho': $("input[type='radio']:checked").attr('id'),
      'strQuery': $('#message').val()
    });
    console.log('click');
  })
  ;
