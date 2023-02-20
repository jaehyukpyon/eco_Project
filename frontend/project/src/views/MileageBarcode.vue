<template>
  <div>
    <div>
      <p>
        <span class="green">녹색매장</span>에서<br />
        <span class="green">친환경 인증 마크</span><b>제품</b>을<br>구매할 때<br />
        사용할 수 있습니다.
      </p>
    </div>
    <div class="img" style="margin-top: 40px; text-align: center; position: relative;">
      <div v-if="type === 'barcode'">
        <img src="../assets/bar_qr_code/barcode.png" width="220" height="200" alt="" />
        <img class="change" src="../assets/bar_qr_code/change.png" width="50" height="50" style="position: absolute; top: 60px; left: 345px;" @click="changeType">
        <img src="../assets/bar_qr_code/qr_small.png" width="50" height="50" style="position: absolute; top: 0px; left: 330px;">
      </div>
      <div v-if="type === 'qr'">
        <img src="../assets/bar_qr_code/qrcode.png" width="220" height="200" alt="" />
        <img class="change" src="../assets/bar_qr_code/change.png" width="50" height="50" style="position: absolute; top: 60px; left: 345px;" @click="changeType">
        <img src="../assets/bar_qr_code/barcode_small.png" width="50" height="50" style="position: absolute; top: 0px; left: 330px;">
      </div>
    </div>
    <div style="margin-top: 25px; text-align: center;">
      <img src="../assets/greenlogo/greenmarks.png" width="400" height="170" alt="">
    </div>
    <div class="checklist" style="margin-top: 20px;">
      <img class="checklist" src="../assets/greenlogo/checkgreenlist_svg.svg" width="485" height="45" alt="">
    </div>
  </div>
</template>

<script>
export default {
  emits: ["barType"],
  data() {
    return {
      type: 'barcode',
    }
  },
  methods: {
    changeType() {
      if (this.type === 'barcode') this.type = 'qr'
      else if (this.type === 'qr') this.type = 'barcode'
    }
  },
  beforeCreate() {
    this.$emit("barType", "shinhan");
    this.$emit("sendCurrentPath", this.$route.path);
  },
};
</script>

<style scoped>
p {
  text-align: center;
  font-size: 25px;
  margin: 20px;
}
.green {
  color: #25bf8b;
  font-weight: bolder;
}
img.change:hover {
  cursor: pointer;
}

.checklist {
  cursor: pointer;
}
</style>