<template>
  <div>
    <shinhan-navigation-bar></shinhan-navigation-bar>
    <div class="top-wrap">
      <img src="../assets/re100/samsungbio2.png" alt="">
      <img class="buybtn" @click="buyClick" src="../assets/re100/buy2.png" alt="">
    </div>
  </div>
</template>

<script>
import ShinhanNavigationBar from '../components/ShinhanNavigationBar.vue';

export default {
  components: {
    ShinhanNavigationBar,
  },
  data() {
    return {
      click: false,
    };
  },
  methods: {

  },
}
</script>

<style scoped>
.top-wrap {
  width: 480px;
  height: 645px;
  background-color: white;
  text-align: center;
  position: relative;
}

.buybtn {
  position: absolute;
  top: 590px;
  right: 12px;
}

.buybtn:hover {
  cursor: pointer;
}
</style>