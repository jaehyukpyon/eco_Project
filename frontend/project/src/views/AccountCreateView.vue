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
</template>

<style scoped>

.temple {
    background-color: #5BDEB2;
    height: 480px;
}
.title {
    font-family: 'Do Hyeon', sans-serif;
    color: white;
    text-align: center;
    padding-top: 130px;
    font-size: 50px;
}
.title > .small {
    font-size: 40px;
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
