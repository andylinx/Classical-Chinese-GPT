<template>
    <div class="whole">
    <el-switch v-model="value2" class="ml-2" style="--el-switch-on-color: #13ce66; --el-switch-off-color: #ff4949" @change="change_mode"/>
    <el-text class="word" size="large" tag="b">文言文对话模式</el-text>
    </div>
</template>
<script lang="ts" setup>
import { ref } from 'vue'
const value2 = ref(true)
import socketio from '../socket/index';
const change_mode=()=>{
    socketio.emit('Change_mode');
}
</script>

<style scoped>
.whole{
    display: flex;
    flex-direction: column;
    margin-top: 650px;
}
.word{
    margin-top: 10px;
}
</style>