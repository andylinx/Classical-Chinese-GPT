<template>
    <div class="tot">
        <el-container class="pic">
            <el-avatar shape="circle" src='https://pic.imgdb.cn/item/6614d13368eb935713cb6c5b.png' fit="fill"
                @error="errorHandler" style="border: 2px solid #ccc;"/>
        </el-container>
        <el-container class="word">
            <slot name="name"></slot>
        </el-container>
        <el-container class="empty">
        </el-container>
    </div>

</template>

<script lang="ts" setup>
const errorHandler = () => true
</script>

<style scoped>
.tot {
    display: flex;
    align-items: flex-end;
    justify-content: flex-end;
    /* 垂直居中对齐 */
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
    background-color: rgba(255, 255, 255, 0.827);
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