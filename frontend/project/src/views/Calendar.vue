<template>
  <nav>
    <div>
      <img src="../assets/buttons/left_error.svg" alt="" />
    </div>
  </nav>
    <div>
    <div>
        <p>
        <span class="title" style="margin-top:50px; text-align: center; position: relative; width: 100%;">친환경 걷기</span><br />
        <span class="sub" style="margin-top: 0px; text-align: center; position: relative; width:100%;">걸음수와 마일리지를 확인할 수 있습니다!</span>
        </p>
        </div>
    <div class="img"
        style="margin-top: 40px; text-align: center; position: relative;">
        <div v-if="type === 'coin'"></div>
        <img
          src="../assets/calendar/coin.png"
          width="100"
          height="90"
          alt=""/>
        <div style="margin-top: 30px; text-align: center; position: relative;">
        <div v-if="type === 'calendar'"></div>
        <img
          src="../assets/calendar/calendar.png"
          width="420"
          height="370"
          alt=""/>
    </div>
  </div>
  </div>
</template>

<script>
export default {
    data() {
        return{          
        };
    },
    methods: {},
    created() {},
};
</script>
<style scoped>

.title {
  display: inline-block;
  font-weight: bold;
  font-size: 32px;
  position: center;
}
.sub {
  display: inline-block;
  font-weight: light;
  font-size: 15px;
  position: center;
}
nav {
  line-height: 75px;
}
nav > div {
  width: 480px;
  height: 75px;
  background-color: #25bf8b;
}

img {
  display: inline-block;
  vertical-align: middle;
  margin-left: 20px;
}

</style>