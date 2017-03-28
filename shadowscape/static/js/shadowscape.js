/**
 * Created by indralukmana on 28/03/2017.
 */

$(document).ready(function () {

    var socket = io.connect();

    socket.on('connect', function () {
        socket.emit('my event', {data: 'I\'m connected!'});
        console.log(socket.id)
    });

    $('a').on('click', function () {
        socket.emit('day update', {day: $(this).attr('id')});
        return false;
    });

});