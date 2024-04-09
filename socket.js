var http = require('http');
var fs = require('fs');
var spawn = require('child_process').spawn;
var path = require('path');
var childCwd = path.join(__dirname);
const scriptPath = '/mnt/d/cs_courses/Classical-Chinese-GPT/main.py';
const excute = 'python3'
var socketio = require('socket.io')(server);
var child = spawn(excute, [scriptPath],{ cwd: childCwd, encoding: 'utf8' }); //{ cwd: childCwd, encoding: 'utf8' }
const htmldata = fs.readFileSync('./test.html', 'utf-8');
const cssdata = fs.readFileSync('./web.css', 'utf-8');
var server = http.createServer(function (request, response) {
    const styleTag = `<style>${cssdata}</style>`;
    const combineCSS = htmldata.replace(/(<head>|<head[^>]*>)/i, '$1' + styleTag);
    response.writeHead(200, { 'Content-Type': 'text/html' });
    response.end(combineCSS);
}).listen(52036, "0.0.0.0", function () {//
    console.log('服务器监听地址在 http://127.0.0.1:52036');
    child = spawn(excute, [scriptPath],{ cwd: childCwd, encoding: 'utf-8' });
    console.log('子程序接入');
    child.on('spawn', () => {
        console.log('Python 子程序已启动');
    });
});


var io = socketio.listen(server);
io.sockets.on('connection', function (socket) {
    console.log('网页端已接入!');

    socket.on('WebData', function (data) {
        // 将字符串转换为UTF-8编码的Buffer
        const encodedData = Buffer.from(data, 'utf-8');
        console.log('网页端发来的数据是:', encodedData);
        child.stdin.write(encodedData+'\n');
        //child.stdin.end();
        // console.log('网页端发来的数据是:', data);
        // child.stdin.write(data+'\n');
        //child.stdin.end();
    });
    child.stdout.on('data', function (output) {
        var outputString = output.toString('utf-8');
        console.log('result:', outputString);
        socket.emit('serverData', outputString);
    });
});