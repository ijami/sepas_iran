/**
 * Created by Ehsan on 8/20/2015.
 */
$(document).ready(function () {
    var socket = io.connect('http://localhost:8888', {port: 8888});

    var sold_number = $('input[name="sn"]').val();

    var remain_span = $('#remain_count');

    socket.emit('init', {'sold_number':sold_number})

    socket.on("change_capacity", function (data) {
        console.log("haminja");
        var num = parseInt(remain_span.text());
        num = num - parseInt(data['count']);
        remain_span.animate({
            opacity: 0.25,
            fontSize: '2em',
            color: 'red',
        }, 500, function () {
            remain_span.css('opacity', 1);
            remain_span.css('font-size', '1em');
            remain_span.text(num);
        });
        console.log(num);
    });
});