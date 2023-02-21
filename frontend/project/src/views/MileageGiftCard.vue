<template>
  <div>
    <shinhan-navigation-bar></shinhan-navigation-bar>
    <div style="position: relative">
      <img src="../assets/mileage/giftcard10000.png" alt="" />
      <span class="il-man">100,000</span>
    </div>
    <div style="position: relative">
      <img src="../assets/mileage/giftcard30000.png" alt="" />
      <span class="sam-man">300,000</span>
    </div>
    <div class="top-wrap" style="text-align: center">
      <img src="../assets/mileage/notice2.png" alt="" />
      <img src="../assets/mileage/notice3.png" alt="">
    </div>
  </div>
</template>

<script>
import ShinhanNavigationBar from '@/components/ShinhanNavigationBar.vue';
export default {
  components: {
    ShinhanNavigationBar,
  }
};
</script>

<style scoped>
div.top-wrap {
  height: 180px;
  overflow: auto;
}
span {
  position: absolute;
  display: inline-block;
  font-size: 30px;
  font-weight: bolder;
  color: blue;
}
.il-man {
  top: 121px;
  right: 96px;
}

.sam-man {
  top: 121px;
  right: 96px;
}
</style>