<template>
  <el-container class="tot">
    <el-input v-model="textarea" style="width: 240px" :rows="3" type="textarea"
      :placeholder="textarea ? '' : 'Enter to send'" @keydown.enter="EMIT($event)" class="input-text" id="inarea" :style="{
        boxShadow: `var(${getCssVarName('')})`,
      }" />
  </el-container>
</template>

<style scoped>
.tot {
  display: flex;
  flex-direction: row;
}

.input-text {
  flex: 7;
  margin: 10px;
}
</style>

<script lang="ts" setup>
import { ref } from 'vue'
import socketio from '../socket/index';
const textarea = ref('')
const emits = defineEmits(
  ["emitmsg"]
)
const EMIT = (event: KeyboardEvent) => {
  event.preventDefault();
  const text = textarea.value;
  if (text) {
    socketio.emit('User', text);
    emits("emitmsg", text);
    textarea.value = '';
    console.log('we send');
  }
  else {
    console.log('emty message');
  }
}

const getCssVarName = (type: string) => {
  return `--el-box-shadow${type ? '-' : ''}${type}`
}
</script>