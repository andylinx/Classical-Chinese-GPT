<template>
    <div class="whole">
        <el-main class="chat-box" id="t">
            <ChatBox v-for="msg in messages">
                <el-container v-if="msg.isSelf" class="User">
                    <UserMsg>
                        <template #name>
                            <div v-html="msg.content"></div>
                        </template>
                    </UserMsg>
                </el-container>
                <el-container v-if="!msg.isSelf" class="Robot">
                    <RobotMsg>
                        <template #name>
                            <div v-html="msg.content"></div>
                        </template>
                    </RobotMsg>
                </el-container>
            </ChatBox>
        </el-main>
        <el-footer class="the-footer">
            <Footers @emitmsg="emitmsg"></Footers>
        </el-footer>
    </div>
</template>


<script lang="ts" setup>
import { ref } from 'vue'
import Footers from './Footers.vue';
import ChatBox from './ChatBox.vue';
import UserMsg from './UserMsg.vue';
import RobotMsg from './RobotMsg.vue';
import socketio from '../socket';
import { nextTick } from 'vue';

socketio.on('response', (msg: string) => {
    console.log(msg);
    messages.value.push(new Message(msg.replace(/\n/g, '<br>'), false));
})
// 使用Vue的ref来创建响应式数据
class Message {
    content: string
    isSelf: boolean
    constructor(content: string, isSelf: boolean) {
        this.content = content;
        this.isSelf = isSelf;
    }
}
const messages = ref<Message[]>([]);
// const Box = document.getElementById("chat-box")
const emitmsg = (msg: string) => {
    console.log('get ' + msg)
    messages.value.push(new Message(msg.replace(/\n/g, '<br>'), true));
    nextTick(() => {
        const chatContainer = document.getElementById('t');
        if (chatContainer) {
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
    });
}
</script>


<style scoped>
.whole {
    height: 740px;
    display: flex;
    flex-direction: column;
}

.chat-box {
    flex: 6;
    overflow-y: auto;
    /* 允许垂直滚动 */
    height: 300px;
    /* 设置容器的高度 */
    background-color: rgb(240, 240, 240);
}

.the-footer {
    flex: 1;
    background-color: rgb(240, 240, 240);
}

.User {
    width: 100%;
    justify-content: flex-end;
    align-self: flex-end;
    background-color: rgb(240, 240, 240);
}

.Robot {
    width: 100%;
    background-color: rgb(240, 240, 240);
}
</style>