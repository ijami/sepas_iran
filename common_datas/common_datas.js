var express = require('express');
var app = express();
var httpServer = require('http').Server(app);
var io = require('socket.io')(httpServer);
var bodyParser = require('body-parser')
app.use(bodyParser.json());       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
    extended: true
}));

var port = 8888; //different from port that we assign to django server!

var clients = [];
var django_server = null;


app.use('/static', express.static(__dirname + '/template/static'));

app.post('/change_cap', function (req, res) {
    console.log("in server!")
    var count = req.body.count;
    var sold_number = req.body.sold_number;
    if (clients[sold_number]) {
        for (var i in clients[sold_number]) {
            clients[sold_number][i].emit('change_capacity', {'count': count});
        }
    }
    res.send('Hello World!');
});

io.on('connection', function (socket) {
    var sold_number;

    socket.on('init', function (data) {
        sold_number = data['sold_number'];
        if (clients[sold_number]) {
            clients[sold_number].push(socket);
        } else {
            clients[sold_number] = [socket]
        }
    });
    console.log("new client");

    socket.on('disconnect', function () {
        if (sold_number) {
            var index = clients[sold_number].indexOf(socket);
            if (index > -1) {
                clients[sold_number].splice(index, 1);
            }
            console.log("went client");
        }
    });
});


httpServer.listen(port, function () {
    console.log('listening on port ' + port);
});