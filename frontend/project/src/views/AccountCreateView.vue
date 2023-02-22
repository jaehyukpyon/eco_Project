<template>
    <meta charset="UTF-8">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap" rel="stylesheet">
    <green-bar></green-bar>
    <div class="temple">
        <p class="title">친환경 계좌 <br>
            <span class="small">개설하고</span> <br>
            마일리지<span class="small">도 받자!</span> </p>
    </div>
    <div class="sub">
        <p class="subtitle" style="margin-left:15px; margin-top: 5px; text-align:left; position:relative;">친환경 계좌 개설하면<br>
            <span class="subtitle1">마일리지 지급</span><br>
            <span class="subtitle2" style="margin-left:370px; margin-top:0px; text-align:right;">마일리지로</span><br>
            <span class="subtitle3" style="margin-left:370px; text-align:right;" >친환경</span>
            <span class="subtitle4">주식도!</span></p>
    </div>
        <button @click="create" style="margin-top: 5px;">친환경 계좌 개설하기</button>
    
</template>

<style scoped>

.temple {
    background-color: #5BDEB2;
    height: 470px;
}
.temple2 {
    background-color: #25BF8B;
    height: 100px;
}
.title {
    font-family: 'Do Hyeon', sans-serif;
    color: white;
    text-align: center;
    padding-top: 130px;
    font-size: 50px;
}
button {
    background-color: #25BF8B;
    color: white;
    padding: 17px 20px;
    margin: 8px 0;
    border: none;
    cursor: pointer;
    width: 100%;
    font-size: 1.2rem;
  }

.title > .small {
    font-size: 40px;
}
.subtitle {
    font-size: 20px;
    position: left;
    font-weight: 500;
}
.subtitle1 {
    font-size: 20px;
    position: left;
    font-weight: 500;
}
.subtitle2 {
    font-size: 17px;
    position: right;
    font-weight: Medium;
}
.subtitle3 {
    font-size: 17px;
    position: right;
    font-weight: Medium;
    color: #25BF8B;
}
.subtitle4 {
    font-size: 17px;
    position: right;
    font-weight: Medium;
}
</style>

<script>
    import GreenBar from "../components/GreenBar.vue";
    export default {
        components: {
            GreenBar,
        }
    };
</script>
