<link rel="preconnect" href="https://fonts.googleapis.com"></link>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin></link>
<link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@900&family=Noto+Sans+KR:wght@100;400&display=swap" rel="stylesheet"></link>

<template>
    <greenbar></greenbar>
    <div class="temple">
        <p style="font-family: 'Noto Sans KR', sans-serif">친환경 계좌</p>
    </div>
</template>

<style>

.temple {
    background-color: #5BDEB2;
    height: 480px;
}
</style>

<script>
    import GreenBar from "../components/GreenBar.vue";
    export default {
    emits: ["barType"],
    data() {
        return {
        }
    },
    methods: {

    },
    beforeCreate() {
        this.$emit("barType", "green");
        this.$emit("sendCurrentPath", this.$route.path);
    },
    };
</script>
