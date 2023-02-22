<template>
    <meta charset="UTF-8">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap" rel="stylesheet">
    <green-bar></green-bar>
    <div class="temple">
        <p class="title">인식된 <b>신분증 정보</b>를 확인하고<br> 잘못된 경우 <b>직접 수정</b>해주세요! </p>
    </div>
    <div class="container">
    <div style="text-align: center;">
    </div>

    <label for="name"><b>이름</b></label>
    <input type="text" placeholder="가입하실 이름을 입력해주세요." />
    
    <label for=""><b>주민번호</b></label>
    <input type="number" placeholder="주민번호를 입력해주세요." />

    <label for="date"><b>발급일자</b></label>
    <input type="number" placeholder="받급 받으실 날짜를 입력해주세요." />

    </div>
    <button @click="next" style="margin-top: 45px;">다음</button>
</template>


<style scoped>
  input[type="text"],
  input[type="number"] {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    box-sizing: border-box;
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
  .container {
    padding: 16px;
  }

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
        },
        methods: {
            confirm() {
                const name= this.$refs.name.value;
                const number=this.$refs.number.value;
                const date= this.$refs.date.value;
            },
            next() {
                this.$router.push('/account/done')
            }
        }
        
    };
</script>
