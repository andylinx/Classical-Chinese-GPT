<template>
    <div class="tot">
        <el-container class="empty">
        </el-container>
        <el-container class="word">
            <slot name="name"></slot>
        </el-container>
    </div>
    <el-container class="pic">
        <el-avatar shape="circle" src='https://pic.imgdb.cn/item/6614d29b68eb935713cce02b.png' fit="fill"
            @error="errorHandler" style="border: 2px solid #ccc;"/>
    </el-container>
    <!-- src='https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg' -->
</template>

<script lang="ts" setup>
const errorHandler = () => true
</script>

<style scoped>
.tot {
    display: flex;
    width: 100%;
    background-color: rgb(240, 240, 240);
    ;
    margin: 15px;
}

.empty {
    flex: 100;
}

.word {
    font-family: Microsoft YaHei;
    word-break: break-word;
    font-size: medium;
    color: rgb(255, 255, 255);
    background-color: rgb(18, 58, 255);
    word-wrap: break-word;
    white-space: normal;
    max-width: 400px;
    padding: 15px;
    margin-right: 10px;
    border-radius: 10px;
}

.pic {
    width: 50px;
    align-self: center;
    margin: 10px;
}
</style>