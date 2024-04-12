<template>
    <div class="whole">
        <img src="../assets/wen.jpg" alt="?" class="head-pic">
        <div class="r">
            <div class="text">
                <el-text tag="b" size="large">问 · 道</el-text>
            </div>
            <div class="user_part">
                <div class="user_name"><el-text class="mx-1" tag="b" type="info">计算机科学家</el-text></div>
                <div class="pic">
                    <el-avatar shape="circle" src='https://pic.imgdb.cn/item/6614d29b68eb935713cce02b.png' fit="fill"
                        style="border: 2px solid #ccc;" />
                </div>
            </div>
        </div>
    </div>
</template>
<style scoped>
.whole {
    height: 90px;
    display: flex;
}

.head-pic {
    margin-left: 100px;
    height: 100%;
}

.r {
    width: 100%;
    display: flex;
    align-self: center;
    margin-right: 30px;
}

.text {
    flex: 10;
    margin-left: 440px;
    font-size: large;
}
.user_part{
    flex:4;
    display: flex;
    align-self: center;
}

.user_name {
    flex: 3;
    margin-top: 6px;
}

.pic {
    flex: 1;
    margin-right: 20px;
}
</style>