<template>
    <el-container class="whole">
        <div class="tag1">
            <img src="../assets/tag1.jpg" alt="no img" class="t1">
        </div>
        <div class="tag2">
            <img src="../assets/rock.jpg" alt="no img" class="t2">
        </div>
        <div class="tag3">
            <img src="../assets/tag1.jpg" alt="no img" class="t3">
        </div>
    </el-container>
</template>
<script lang="ts" setup>
</script>

<style scoped>
.whole {
    display: flex;
    flex-direction: column;
    width: 100%;
}

.tag1 {
    background-color: rgb(207, 207, 207);
    margin: 30px;
    margin-top: 60px;
    margin-left: 130px;
    margin-right: 230px;
    flex: 3;
    border-radius: 10px;
}
.t1{
height: 150px;
border-radius: 10px;
}
.t2{
height: 150px;
border-radius: 10px;
}
.t3{
height: 150px;
border-radius: 10px;
}

.tag2 {
    background-color: rgb(207, 207, 207);
    margin: 30px;
    margin-left: 330px;
    flex: 3;
    border-radius: 10px;
}

.tag3 {
    background-color: rgb(207, 207, 207);
    margin: 30px;
    margin-left: 200px;
    margin-right: 160px;
    flex: 3;
    border-radius: 10px;
}
</style>