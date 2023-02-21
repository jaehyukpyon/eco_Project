<template>
    <meta charset="UTF-8">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap" rel="stylesheet">
    <green-bar></green-bar>
    <div class="temple">
        <p class="title">인식된 <b>신분증 정보</b>를 확인하고<br> 잘못된 경우 <b>직접 수정</b>해주세요! </p>
    </div>
    <div class="input_div">
        <input type="text" name="username" hint="이름"> 
        <input type="text" name="number" hint="주민번호"> 
        <input type="text" name="date" hint="날짜">
    </div>
</template>

<style scoped>
    .temple {
        height: 250px;
    }
    .title {
        font-family: 'Do Hyeon', sans-serif;
        text-align: center;
        padding-top: 90px;
        font-size: 25px;
    }
    .input_div {
        display: flex;
        justify-content: center;
        padding-top: 20px;
        height: 400px;
    }
    .input_div > input {
        height: 100px;
        width: 300px;
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
