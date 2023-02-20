<template>
  <shinhan-navigation-bar></shinhan-navigation-bar>
  <section class="home-mileage">
    <div style="text-align: center">
      <p style="font-size: 2rem; color: white">친환경 마일리지</p>
    </div>

    <div style="text-align: center; margin: 30px 0px">
      <span>0</span>&nbsp;포인트
    </div>

    <div style="margin-bottom: 20px">
      <table class="mileage-menu">
        <tbody>
          <tr>
            <td><a>마일리지 내역</a></td>
            <td><a href="">마일리지 사용</a></td>
          </tr>
          <tr>
            <td><a href="">친환경 걷기</a></td>
            <td><a href="">미션</a></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="temperature">
      <div>
        <p style="display: inline-block; color: white">
          <span>이관현</span>님의 친환경 온도&nbsp;&nbsp;
        </p>
        <p style="display: inline-block; color: white">
          <span>35&#8451;</span>
        </p>
      </div>
    </div>

    <div class="sub-menus" style="margin-top: 30px">
      <div class="item">
        <img :src="require('../assets/cards/card1.png')" alt="" />
      </div>
      <div class="item">
        <img :src="require('../assets/cards/card2.png')" alt="" />
      </div>
      <div class="item">
        <img :src="require('../assets/cards/card3.png')" alt="" />
      </div>
    </div>
  </section>
</template>

<script>
import ShinhanNavigationBar from '../components/ShinhanNavigationBar.vue'
export default {
  // emits: ["sendCurrentPath", 'barType',],
  // beforeCreate() {
  //   this.$emit("sendCurrentPath", this.$route.path);
  //   this.$emit('barType', 'shinhan');
  // },
  components: {
    ShinhanNavigationBar,
  },
  data() {

  }
};
</script>

<style scoped>
.temperature {
  width: 412px;
  height: 52px;
  line-height: 52px;
  margin: 0 auto;
  background-color: #1e996f;
  border-radius: 20px;
}

.temperature > div {
  text-align: center;
}
.home-mileage {
  background-color: #5bdeb2;
}

.mileage-menu {
  margin: 0 auto;
  border-collapse: collapse;
  border-style: hidden;
}

.mileage-menu td {
  padding: 1rem;
  border: 1px solid black;
  text-align: center;
}

.home-mileage > div:first-child {
  padding: 20px 0px 0px;
}

.sub-menus {
  max-height: 200px;
  display: flex;
  overflow-x: auto;
}
.sub-menus .item:first-child {
  margin-left: 20px;
}
.sub-menus .item {
  min-width: 180px;
  height: 180px;
  line-height: 180px;
  text-align: center;
  background-color: green;
  margin-right: 20px;
}

.sub-menus img {
  width: 100%;
  height: 100%;
}
/* https://blog.hubspot.com/website/center-div-css */
</style>