<template>
  <div class="common-layout">
    <el-container>
      <el-header class="header">
        <Headers />
      </el-header>
      <el-container class="down-part">
        <el-aside class="left">
          <Left />
        </el-aside>
        <el-container class="right-part">
          <el-container class="main-part">
            <ChatPage />
          </el-container>
          <el-container class="right-col">
            <Right />
          </el-container>
        </el-container>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped>
.common-layout {
  width: 100%;
  display: flex;
  height: 800px;
  flex-direction: column;
  background-color: aquamarine;
}

.header {
  flex: 3;
  width: 100%;
  align-self: center;
  background-color: rgb(240, 240, 240);
}

.down-part {
  flex: 9;
  display: flex;
  flex-direction: row;
}

.left {
  flex: 3;
  background-color: rgb(240, 240, 240);
}

.main-part {
  flex: 10;
  display: flex;
  flex-direction: column;
}

.right-part{
  flex: 10;
  display: flex;
  flex-direction: row;
}

.right-col{
  flex: 3;
  background-color: rgb(240, 240, 240);
}

</style>


<script setup>
import Left from './components/Left.vue';
import ChatPage from './components/ChatPage.vue';
import Headers from './components/Headers.vue';
import socketio from './socket/index';
import Right from './components/Right.vue';
</script>