var spawn = require('child_process').spawn;
var path = require('path');
var childCwd = path.join(__dirname);
const scriptPath = './main.py';
const excute = 'python'

const express = require('express')
const http = require('http');
const socketIO = require('socket.io');
const app = express();
const server = http.createServer(app);

var child = spawn(excute, [scriptPath], { cwd: childCwd, encoding: 'utf8' });
console.log('子进程接入');


let mode=true;
const io = socketIO(server, {
    cors: {
        origin: '*'
    }
});


app.get('/', (request, response) => {
    io.emit('message', '服务端向客户端推送消息...');
    response.writeHead(200, { "Content-type": "text/plain" });
    response.end();
});

io.on('connection', (socket) => {
    console.log('user connected');
    mode = true
    socket.on("User", (msg) => {
        console.log('Send was pressed...');
        console.log(msg);
        if(mode){
            console.log('mode 1');
            msg="1"+msg;
        }
        else{
            console.log('mode 0');
            msg="0"+msg;
        }
        const encodedData = Buffer.from(msg, 'utf-8');
        console.log('网页端发来的数据是:', encodedData);
        child.stdin.write(encodedData+'\n');
    });
    socket.on('Change_mode',()=>{
        mode=!mode;
    })
    child.stdout.on('data', function (output) {
        console.log('result:', output.toString());
        io.emit('response', output.toString());
    });
});


server.listen(3001, () => {
    console.log("server is up and running on port 3001");
});