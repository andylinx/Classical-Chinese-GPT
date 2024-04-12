import { io } from 'socket.io-client';
const socketio = io('http://localhost:3001', {
  transports: ['websocket'], // 指定传输方式，如WebSocket
  autoConnect: true, // 是否自动连接
  reconnection: true, // 是否自动重新连接
  reconnectionAttempts: 3, // 重新连接尝试次数
  reconnectionDelay: 1000, // 重新连接延迟时间（毫秒）
  query: { token: 'wen_dao' }, // 自定义查询参数
});
socketio.on('connect', () => {
  console.log("连接！");
});
export default socketio