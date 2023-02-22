<template>
    <div class="temple">
        <p class="title">친환경 계좌 <br>
            <span class="small">완료되었습니다!</span> 
        </p>
    </div>
<span class="sub" style="margin-top: 0px; text-align: center; position: relative; width:100%;">친환경 계좌 개설 완료!</span>
<div v-if="type === 'account'"></div>
        <img
          src="../assets/account/account.png"
          width="480"
          height="160"
          alt=""
        />
<div class="done">
    <button id="confrim" v-on:click="btn_confrim">확인</button>
</div>
</template>

<script>
export default {
    data() {
        return {
            name: 'done',
        }
    },
    methods: {
        btn_confrim: function(event) {
            alert('개설 완료!')
        }
    }
}
</script>

<style scoped>
.sub {
  display: inline-block;
  font-weight: light;
  font-size: 15px;
  position: center;
}
.done {
    display: inline-block;
    font: bold;
    font-size: 20px;
    color: white;
    position: center;
    background-color: #25bf8b;
}
.temple {
    background-color: #5BDEB2;
    height: 480px;
}

</style>