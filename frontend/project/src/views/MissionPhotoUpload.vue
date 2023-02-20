<template>
  <div>
    <div class="top-wrap">
      <img src="../assets/missionphotoupload/greenrectangle.png" alt="" />
      <div class="mission-text">
        <p>
          <span class="mission-type">텀블러 사용하기</span><br /><br />
          <span class="mission-description"
            >카페에서 텀블러를<br />사용한 사진을<br />업로드 해주세요!</span
          >
        </p>
      </div>
    </div>

    <div class="image-wrap">
      <div class="image-thumbnail">

      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  methods: {},
  beforeCreate() {
    this.$emit("sendCurrentPath", this.$route.path);
    this.$emit("barType", "shinhan");
  },
};
</script>

<style scoped>
.image-thumbnail {
  margin-top: 20px;
  margin-left: 16px;
  width: 450px;
  height: 360px;
  background-color:antiquewhite;
  border-radius: 20px;
}
.mission-type {
  font-size: 1.5rem;
}

.mission-description {
  font-size: 1.2rem;
}
.top-wrap {
  margin-top: 20px;
  position: relative;
  text-align: center;
}
.top-wrap .mission-text {
  display: flex;
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  align-items: center;
  justify-content: center;
}
</style>